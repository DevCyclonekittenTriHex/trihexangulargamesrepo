from CTkMessagebox import CTkMessagebox
import customtkinter as ctk

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
global rt
rt=""
def MENU():
    global rt
    rt = ctk.CTk()
    lb = ctk.CTkLabel(master=rt,text="Updating...")
    lb.place(x=50,y=50)
    rt.update()

def KillUpdateWindow():
    global rt
    rt.destroy()