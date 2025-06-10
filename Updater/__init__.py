import os
home_dir = os.path.expanduser("~")

try:
    f=open(os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater","settings.json"),"r")
    f.read()
    f.close()
    
    print("UpdaterInstalled")
    import main
    main.skipstep = True
except Exception as e:
    print("Not Installed")
    import maingui
    maingui.L1()