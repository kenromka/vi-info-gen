import contextlib
import requests
import time

__all__ = ['yadisk_upload']

class SelfDestructingSession(requests.Session):
    """Regular `requests.Session` but with a destructor"""

    def __init__(self, *args, **kwargs):
        self._init_completed = False

        requests.Session.__init__(self, *args, **kwargs)

        self._init_completed = True

    def __del__(self):
        if self._init_completed:
            if hasattr(requests.Session, "__del__"):
                requests.Session.__del__(self)

            self.close()

def auto_retry(func, n_retries=3, retry_interval=0.0, **kwargs):
    for i in range(n_retries + 1):
        try:
            return func()
        except (requests.exceptions.RequestException) as e:
            if i == n_retries:
                raise e

        if retry_interval:
            time.sleep(retry_interval)

def get_upload_link(session, path, overwrite=True, fields=None, **kwargs):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded'

    data = {}

    params = {}
    params['path'] = path
    params['overwrite'] = "true" if overwrite else "false"
    
    if fields is not None:
        params['fields'] = ','.join(fields)
  
    r = requests.Request(method=method, url=url,
                         data=data, params=params)
    r.headers['Content-Type'] = content_type
    request = session.prepare_request(r)

    def dummy():
        return session.send(request)
    
    response = auto_retry(
        dummy,
        **kwargs
    )

    return response
    # .process().href

def upload(session, file_path, dest_path, **kwargs):
    kwargs = dict(kwargs)

    timeout = kwargs.get('timeout', (10.0, 15.0))
    retry_interval = kwargs.get('retry_interval', 0.0)
    n_retries = kwargs.get('n_retries', 3)
    kwargs['timeout'] = timeout

    file = None

    try:
        file = open(file_path, 'rb')
        file_position = file.tell()

        def attempt():
            temp_kwargs = dict(kwargs)
            temp_kwargs['n_retries'] = 0
            temp_kwargs['retry_interval'] = 0.0

            link = get_upload_link(session, dest_path, **temp_kwargs).json().get('href', None)

            for k in ('n_retries', 'retry_interval', 'overwrite', 'fields'):
                temp_kwargs.pop(k, None)

            temp_kwargs.setdefault('stream', True)

            try:
                temp_kwargs['headers'].setdefault('Connection', 'close')
            except KeyError:
                temp_kwargs['headers'] = {'Connection': 'close'}

            file.seek(file_position)

            with contextlib.closing(session.put(link, data=file, **temp_kwargs)) as response:
                if response.status_code != 201:
                    print('yadisk.upload()', '_'*10)
                    print(response.json())
                    raise Exception
            
        auto_retry(attempt, n_retries, retry_interval)
    finally:
        if file is not None:
            file.close()

def yadisk_upload(token='AgAAAAA31yxcAAXhxQuR1R2CAERVtoo-Klf_gIs', file_path='', dest_path=''):
    
    session = SelfDestructingSession()
    
    if token:
        session.headers['Authorization'] = 'OAuth ' + token

    return upload(session, file_path, dest_path)