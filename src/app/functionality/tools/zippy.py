import zipfile
import os

def zippify(target, out):
    """
    Архивация содержимого папки


    Аргументы:
        target (str): путь к папке, которую
            необходимо заархивировать

        out    (str): путь к файлу, в который
            будет записан архив. 
            (ПРИМЕЧАНИЕ: при существовании файла
            с таким же именем он будет перезаписан
        
    """
    
    z = zipfile.ZipFile(out, 'w')
    for root, dirs, files in os.walk(target):
        for file in files:
            z.write(os.path.join(root,file))
    
    z.close()

touch_folder = lambda folder: os.mkdir(folder) if not os.path.exists(folder) else True
check_folder = lambda folder: not os.listdir(folder)
