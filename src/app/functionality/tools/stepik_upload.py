api_url = 'https://stepik.org/api/step-sources'
auth_url = 'https://stepik.org/oauth2/token/'
step_url = 'https://stepik.org/lesson/{lesson_id}/step/{step_id}'

def upload2lesson(client_id, client_secret, lesson_id, position, data):

    import json
    import requests

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    resp = requests.post(
        auth_url, 
        data={
            'grant_type': 'client_credentials'
        }, 
        auth=auth
    )
    token = json.loads(resp.text)['access_token']

    full_data = {
        'stepSource': {
            'block': data,
            'lesson': lesson_id,
            'position': position
        }
    }

    r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=full_data)

    step_id = r.json()['step-sources'][0]['id']
    return step_url.format(
        lesson_id = lesson_id,
        step_id = 1
    )