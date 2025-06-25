import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

rt = ""
def Install():
    global rt
    rt.destroy()
    import main

def Settings():
    global btns
    for i in btns:
        i.place_forget()
    print("Settings")
btns = []
def ask_question():
    msg = CTkMessagebox(title="Launcher Outdated", message="Trihexangular Launcher outdated or not installed, do you want to download the latest version.",
                        icon="question", option_1="Update", option_2="Run", option_3="Exit")
    response = msg.get()
    
    if response=="Update":
        return 2
    elif response=="Run":
        return 1
    elif response=="Exit":
        return 0
def L1():
    global rt
    rt = ctk.CTk()
    rt.geometry("200x300")
    label = ctk.CTkLabel(master=rt,text="Trihexangular Installer")
    label.place(x=35,y=0)
    ibtn = ctk.CTkButton(master=rt,text="Install Launcher", width=100, height=30,command = Install)
    ibtn.place(x=50,y=150)
    sbtn = ctk.CTkButton(master=rt,text="Settings", width=100, height=30,command = Settings)
    sbtn.place(x=50,y=200)
    qbtn = ctk.CTkButton(master=rt,text="Quit", width=100, height=30,command = lambda:rt.destroy())
    qbtn.place(x=50,y=250)
    global btns
    btns = [ibtn,sbtn,qbtn,label]
    
    rt.mainloop()