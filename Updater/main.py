import downloader,os,json,subprocess
import data as dat
import gui



home_dir = os.path.expanduser("~")
if not home_dir:
    exit()


try:
    data = dat.Data(False)
except Exception as e:
    try:
        os.makedirs(os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater"))
    except Exception as r:
        pass
    f=open(os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater","settings.json"),"w")
    f.write(json.dumps({"version":-1,"run-after-update":True},indent=4))
    f.close()
    data = dat.Data(False)

# Get Launcher Data
try:
    os.makedirs(os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater","Downloading"))
except Exception as f:
    pass
link = "https://github.com/DevCyclonekittenTriHex/trihexangulargamesrepo/raw/main/Data/launcher_package.zip"
zipp = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater","Downloading","Packages.zip")
extr = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater")
response = downloader.install_github_link(link,zipp,extr)

lpdata = dat.Data(os.path.join(extr,"launcher_package.json"))


def UpdateChecker():
    if(data.GetVersion()<lpdata.GetVersion()): #Outdated
        return True
    else:
        return False
def Install():
    global home_dir
    link = "https://github.com/DevCyclonekittenTriHex/trihexangulargamesrepo/releases/download/main_update/All_In_One_ZIP.zip"
    zipp = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater","Downloading","Launcher.zip")
    extr = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Launcher","bin")
    downloader.install_github_link(link,zipp,extr)
    print(lpdata.GetVersion())
    data.SetVersion(lpdata.GetVersion())
import time
def Run():
    global home_dir
    launcher_path = project_path = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Launcher")
    os.makedirs(launcher_path, exist_ok=True)
    os.makedirs(os.path.join(launcher_path,"bin"), exist_ok=True)
    path = os.path.join(launcher_path,"bin","Trihexangular Launcher.exe")
    subprocess.Popen([path])
time.sleep(0.1)
skipstep = False
def MainLoop():
    __update__ = UpdateChecker()

    if __update__ or skipstep==True:
        if(skipstep==True):
            respon = 2
        else:
            respon = gui.ask_question()
        if(respon==2):
            gui.MENU()
            Install()
            gui.KillUpdateWindow()
            if(data.RunAfterUpdate()):
                Run()
        elif(respon==1):
            Run()

        else:
            exit()
    else:
        Run()

MainLoop()