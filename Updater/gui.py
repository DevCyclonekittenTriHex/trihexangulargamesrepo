


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