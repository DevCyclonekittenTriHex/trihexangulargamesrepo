import customtkinter as ctk


def Install():
    rt.destroy()
    import main

def Settings():
    global btns
    for i in btns:
        i.place_forget()
    print("Settings")

def L1():
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

    btns = [ibtn,sbtn,qbtn,label]
    rt.mainloop()