from tkinter import *
from tkinter import messagebox
import sys
import webbrowser
import cv2
import keyboard
def AbutTheDeveloper():
    img = cv2.imread("cv.png")
    cv2.imshow("Abut the developer", img)
    cv2.waitKey(0)
def facebook():
    webbrowser.open_new_tab('https://www.facebook.com/profile.php?id=100091559190845')
def instagram():
    webbrowser.open_new_tab('https://www.instagram.com/omar124219')
def github():
    webbrowser.open_new_tab('https://github.com/Omarpython')
def ProgrammerRights():
    """ حقوق المبرمج  Programmer Rights"""
    img = cv2.imread("Social.png")
    cv2.imshow("Programmer Rights", img)
    cv2.waitKey(0)
vid = cv2.VideoCapture("E:\\corsat\\tkinter_py\\1.mp4")
def ExplanatoryVideo():
    """ Explanatory Video فيديو توضيحي """
    while keyboard.is_pressed('q') == False:
        _, img = vid.read()
        cv2.imshow("Explanatory Video", img)
        cv2.waitKey(1)
passw = Tk()
passw.title('Password Social App')
passw.geometry("801x490+380+150")
passw.iconbitmap('ico.ico')
passw.resizable(False,False)
passw.configure(bg="white")
photo = PhotoImage(file='Social.png')
panel = Label(passw, image=photo)
panel.place(x=1, y=1, width=600, height=320)
frameWeb = Frame(passw, bg='orange')
frameWeb.place(x=603, y=-1, width=200, height=560)
lblone = Label(frameWeb, text="Welcome", fg='black', font=('Playfair Display',16), background='orange')
lblone.place(x=50, y=10)
lbltwe = Label(frameWeb, text="Welcome to the social", fg='black', font=('Playfair Display',12), background='orange')
lbltwe.place(x=19, y=40)
lblThree = Label(frameWeb, text=" media application", fg='black', font=('DynaPuff',12), background='orange')
lblThree.place(x=30, y=70)
buttonexit = Button(frameWeb, text='Abut the developer', background='orange', fg='black', font=('Playfair Display',11), command=AbutTheDeveloper)
buttonexit.place(x=14, y=130, width=170, height=40)
buttonFacebook = Button(frameWeb, text='Facebook', background='orange', fg='black', font=('Playfair Display',11), command=facebook)
buttonFacebook.place(x=14, y=180, width=170, height=40)
buttoninsta = Button(frameWeb, text='Instagram', background='orange', fg='black', font=('Playfair Display',11), command=instagram)
buttoninsta.place(x=14, y=230, width=170, height=40)
buttongithub = Button(frameWeb, text='Github', background='orange', fg='black', font=('Playfair Display',11), command=github)
buttongithub.place(x=14, y=280, width=170, height=40)
buttongithub = Button(frameWeb, text='Programmer Rights', background='orange', fg='black', font=('Playfair Display',11), command=ProgrammerRights)
buttongithub.place(x=14, y=330, width=170, height=40)
buttongithub = Button(frameWeb, text='Explanatory Video', background='orange', fg='black', font=('Playfair Display',11), command=ExplanatoryVideo)
buttongithub.place(x=14, y=380, width=170, height=40)
buttonexit = Button(frameWeb, text='Exit', background='orange', fg='black', font=('Playfair Display',11), command=sys.exit)
buttonexit.place(x=14, y=430, width=170, height=40)
frameEntryPassword = Frame(passw, bg='orange')
frameEntryPassword.place(x=1, y=325,  width=601, height=190)
frameLogo = Frame(frameEntryPassword)
frameLogo.place(x=425, y=-1, width=180, height=180)
photo2 = PhotoImage(file='logo.png')
panel2 = Label(frameLogo, image=photo2, background='orange')
panel2.pack()
lblName = Label(frameEntryPassword, text='Name', bg='orange', background='orange', fg='black', font=('Playfair Display',11))
lblName.place(x=280, y=5)
entryName = Entry(frameEntryPassword, justify=CENTER)
entryName.place(x=190, y=30, width=220, height=25)
lblName = Label(frameEntryPassword, text='Password', bg='orange', background='orange', fg='black', font=('Playfair Display',11))
lblName.place(x=270, y=70)
entrypass = Entry(frameEntryPassword, justify=CENTER)
entrypass.place(x=190, y=100, width=220, height=25)
def log():
    userName = entryName.get()
    password = entrypass.get()
    if userName.lower() == 'admen' and password.lower() == 'admen':
        messagebox.showinfo("welcome", "welcome to Social Applecation")
    elif userName == '' and password == '':
        pass
    else:
        messagebox.showerror('Error', 'The username or password is incorrect')
buttonNexit = Button(frameEntryPassword, text='login', background='orange', fg='black', font=('Playfair Display',11), command=log)
buttonNexit.place(x=15 , y=20 , width=130 , height=120)
passw.mainloop()