from platform import system
from main_PrintFunctions import startSystem1, startSystem2, startSystem3
from main_PrintFunctions import OSERROR
if system().lower() != 'windows': OSERROR()
import os
from threading import Thread
from configure__main import Pathlib_y, Applicator
from applicate__main import Application
from assistant import Assistant

localpath = Pathlib_y.get_mainLOCALpath()
temppath = Pathlib_y.get_mainTEMPpath()
voicepath = Pathlib_y.get_voicePatternspath()
localpath, temppath = Pathlib_y.get_mainLOCALpath(), Pathlib_y.get_mainTEMPpath()
startSystem1()
if not os.path.exists(localpath): os.mkdir(localpath)
if not os.path.exists(temppath) : os.mkdir(temppath)
if not os.path.exists(voicepath): os.mkdir(voicepath)
startSystem2()
if not Applicator.application['settings']['load']: Applicator.reloadAppList()
startSystem3(Applicator.applicationcount, localpath, temppath)
assistante = Assistant()
applicate = Thread(target=Application, daemon=True)

if __name__ == "__main__":
    applicate.start()
    assistante.start_while()