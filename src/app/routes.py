from flask import render_template, request, redirect, url_for, send_file, Response

from .functionality.common import *
from .functionality.tools.task import *
from .functionality.tools.stepik_upload import *

from .functionality.ege import *
from .functionality.oge import *

from .functionality.common import *

from app import app

import time

last_update = "17.08.2019"
DOWNLOAD_PATH = "/tmp/exam-tasks.{extension}"
XTRAS_PATH = "/tmp/xtras/"

exporting_threads = ExportingThread(DOWNLOAD_PATH.format(extension='pdf'), [], {}, "ОГЭ", True, "ans_yes", {})

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", date=last_update)

def filter_tasks(dic, chck_lst):
    res = {}
    for task, task_i in dic.items():
        for typo, typo_i in task_i[0].items():
            for subtype, val in typo_i.items():
                if val[0] in chck_lst:
                    res[task] = res.get(task, ({}, task_i[1]))
                    res[task][0][typo] = res[task][0].get(typo, {})
                    res[task][0][typo][subtype] = val
    return res

@app.route("/ege", methods=["GET", "POST"])
def ege():
    tasks = {}
    dumpys = {}
    for task in BaseTask.__subclasses__():
        real_task = task()
        tasks[real_task.category()] = ({}, set())
        for typo in task.__subclasses__():
            real_typo = typo()
            tasks[real_task.category()][0][real_typo.category()] = {}
            for subtype in typo.__subclasses__():
                real_subtype = subtype()
                tasks[real_task.category()][0][real_typo.category()][pickle.dumps(subtype)] = (real_subtype.category(), real_subtype.level(), real_subtype.max_qty)
                dumpys[real_subtype.category()] = subtype
    if request.method == 'POST':
        if request.form["btn"] == "подтвердить":
            answer = request.form.getlist('subtype')
            return quantity("ЕГЭ", tasks, answer)
        elif request.form["btn"] == "скачать":
            results = []
            headers = False
            answers = "ans_yes"
            proglangs = {}
            global extension
            extension = "pdf"
            for answer, qty in dict(request.form).items():
                if answer in dumpys.keys():
                    qt = qty
                    if isinstance(qty, (list, tuple)):
                        qt = qty[0]
                    results.append((dumpys[answer], int(qt)))
                elif answer == "extension":
                    extension = qty
                    if isinstance(qty, (list, tuple)):
                        extension = qty[0]
                elif answer == "answers":
                    answers = qty
                    if isinstance(qty, (list, tuple)):
                        answers = qty[0]
                elif answer == "headers":
                    headers = True
                elif any(map(lambda x: answer.startswith(x), ("python", "cpplus", "qbasic", "algori", "pascal"))):
                    proglangs[answer[6:]] = proglangs.get(answer[6:], [])
                    proglangs[answer[6:]].append(answer[:6])

            global exporting_threads

            thread_id = randint(1, 1000)
            #PROBLEM OF KILLING THREAD try _stop daemon + exceptions
            try:
                exporting_threads._stop()
            except Exception:
                try:
                    exporting_threads.daemon = True
                except Exception:
                    pass

            exporting_threads = ExportingThread(DOWNLOAD_PATH.format(extension=extension), results, tasks, "ЕГЭ", headers, answers, proglangs)
            exporting_threads.start()

            return redirect(url_for("generate", task_id=thread_id))

    return render_template("choose.html", title="ЕГЭ", date=last_update, tasks=tasks)

def quantity(title, tasks, answer):
    return render_template("quantity.html", title=title, date=last_update, tasks=filter_tasks(tasks, answer))

@app.route("/oge", methods=["GET", "POST"])
def oge():
    tasks = {}
    dumpys = {}
    for task in BaseTaskOge.__subclasses__():
        real_task = task()
        tasks[real_task.category()] = ({},                  ["proglang" if real_task.category() in (
                                                                                                        "Задание 9", 
                                                                                                        "Задание 10"
                                                                                                    ) else set()])
        for typo in task.__subclasses__():
            real_typo = typo()
            tasks[real_task.category()][0][real_typo.category()] = {}
            for subtype in typo.__subclasses__():
                real_subtype = subtype()
                tasks[real_task.category()][0][real_typo.category()][pickle.dumps(subtype)] = (
                                                                                real_subtype.category(), 
                                                                                real_subtype.level(), 
                                                                                real_subtype.max_qty
                                                                            )
                dumpys[real_subtype.category()] = subtype

    if request.method == 'POST':
        if request.form["btn"] == "подтвердить":
            answer = request.form.getlist('subtype')
            return quantity("ОГЭ", tasks, answer)
        else:
            results = []
            headers = False
            answers = "ans_yes"
            proglangs = {}
            global extension
            extension = "pdf"
            for answer, qty in dict(request.form).items():
                if answer in dumpys.keys():
                    qt = qty
                    if isinstance(qty, (list, tuple)):
                        qt = qty[0]
                    results.append((dumpys[answer], int(qt)))
                elif answer == "extension":
                    extension = qty
                    if isinstance(qty, (list, tuple)):
                        extension = qty[0]
                elif answer == "answers":
                    answers = qty
                    if isinstance(qty, (list, tuple)):
                        answers = qty[0]
                elif answer == "headers":
                    headers = True
                elif any(map(lambda x: answer.startswith(x), ("python", "cpplus", "qbasic", "algori", "pascal"))):
                    proglangs[answer[6:]] = proglangs.get(answer[6:], [])
                    proglangs[answer[6:]].append(answer[:6])
            
            global exporting_threads
            
            thread_id = randint(1, 1000)
            #PROBLEM OF KILLING THREAD
            exporting_threads = ExportingThread(DOWNLOAD_PATH.format(extension=extension), results, tasks, "ОГЭ", headers, answers, proglangs)
            exporting_threads.start()

            return redirect(url_for("generate", task_id=thread_id))
    return render_template("choose.html", title="ОГЭ", date=last_update, tasks=tasks)

@app.route("/download", methods=["GET"])
def download():
    try:
        if extension == 'pdf':
            return send_file(
                DOWNLOAD_PATH.format(extension=extension), 
                as_attachment=True, 
                mimetype="application/pdf", 
                cache_timeout=-1
            )
        elif extension == 'csv':

            from .functionality.tools.zippy import zippify, check_folder, touch_folder
            
            if touch_folder(XTRAS_PATH) and not check_folder(XTRAS_PATH):
                zippify(XTRAS_PATH, "/tmp/archives/exam-tasks.zip")
                
                from zipfile import ZipFile
                zf = ZipFile('/tmp/archives/exam-tasks.zip', mode='a')
                zf.write(DOWNLOAD_PATH.format(extension=extension))
                zf.close()

                return send_file(
                    '/tmp/archives/exam-tasks.zip', 
                    as_attachment=True, 
                    mimetype="application/zip", 
                    cache_timeout=-1
                )
            else: 
                return send_file(
                    DOWNLOAD_PATH.format(extension=extension), 
                    as_attachment=True, 
                    mimetype="text/csv", 
                    cache_timeout=-1
                )
        elif extension == 'json':
            from .functionality.tools.zippy import zippify, check_folder, touch_folder
            
            if touch_folder(XTRAS_PATH) and not check_folder(XTRAS_PATH):
                zippify(XTRAS_PATH, "/tmp/archives/exam-tasks.zip")
                
                from zipfile import ZipFile
                zf = ZipFile('/tmp/archives/exam-tasks.zip', mode='a')
                zf.write(DOWNLOAD_PATH.format(extension=extension))
                zf.close()

                return send_file(
                    '/tmp/archives/exam-tasks.zip', 
                    as_attachment=True, 
                    mimetype="application/zip", 
                    cache_timeout=-1
                )
            return send_file(
                DOWNLOAD_PATH.format(extension=extension), 
                as_attachment=True, 
                mimetype="text/json", 
                cache_timeout=-1
            )
        else:
            return '{"message": "wrong file format: {e}"}, 400'.format(e=extension)
    except Exception as e:
        return '{"message": "error with file downloading: {e}"}, 400'.format(e=e)

@app.route("/generate/<int:task_id>", methods=["GET"])
def generate(task_id):
    return render_template("generate.html", task_id=task_id, date=last_update)

@app.route('/progress/<int:thread_id>', methods=["GET"])
def progress(thread_id):
    global exporting_threads
    if exporting_threads.progress < 100:
        if exporting_threads.progress < 99:
            exporting_threads.progress += 1
            time.sleep(randint(1, 3))
        return str(exporting_threads.progress)
    return "100"

@app.route("/stepik-upload", methods=["GET", "POST"])
def stepik_upload():
    if request.method == 'POST':
        if request.form["btn"] == "Выгрузить":

            get_item = lambda x: x[0] if isinstance(x, (list, tuple)) else x

            file_flg = True
            
            for k, v in dict(request.form).items():
                if k == "client":
                    client_id = get_item(v)
                elif k == "secret":
                    client_secret = get_item(v)
                elif k == "lesson":
                    lesson_id = int(get_item(v))
                elif k == "extension" and get_item(v) == "last_step":
                    file_flg = False
                elif k == "btn":
                    pass
                else:
                    ValueError("Wat did u send me????")
            
            if file_flg:
                file = request.files.get('stepik_step')      
                data = file.read()
            
            import json
            data = json.loads(data)
            for i, k in enumerate(data):
                link = upload2lesson(client_id, client_secret, lesson_id, i+1, data.get(k))
            return redirect(link)
    return render_template("stepik-upload.html", date=last_update)

##xtra
