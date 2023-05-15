import tkinter.messagebox
from tkinter import *
import check_camera
import Capture_Image
import Train_Image
import Recognize

def checkCamera():
    check_camera.camer()

def CaptureFaces():
    new_window = Toplevel(root)
    new_window.geometry('350x350')
    new_window.config(bg="#88cffa")
    new_window.title('Register ')

    lbl = Label(new_window, text="Enter Pin", bg='#88cffa', font=('times new roman', 10, 'bold'))
    lbl.pack(padx=10, pady=10)
    ent = Entry(new_window, font=('times new roman', 12, 'bold'), textvariable=Id)
    ent.pack(padx=10, pady=5)

    lbl = Label(new_window, text="Enter Name", bg='#88cffa', font=('times new roman', 10, 'bold'))
    lbl.pack(padx=10, pady=10)
    ent = Entry(new_window, font=('times new roman', 12, 'bold'), textvariable=Name)
    ent.pack(padx=10, pady=5)

    lbl = Label(new_window, text="Enter Email ID", bg='#88cffa', font=('times new roman', 10, 'bold'))
    lbl.pack(padx=10, pady=10)
    ent = Entry(new_window, font=('times new roman', 12, 'bold'), textvariable=Email)
    ent.pack(padx=10, pady=5)

    sub_btn = Button(new_window, text="Submit", command=submit, bg='#88cffa', font=('times new roman', 10, 'bold'))
    sub_btn.pack(side=RIGHT, padx=60, pady=40)
    close_btn = Button(new_window, text="Close Me", command=lambda : new_window.destroy(), bg='#88cffa', font=('times new roman', 10, 'bold'))
    close_btn.pack(side=RIGHT, padx=60, pady=40)

def Trainimages():
    Train_Image.TrainImages()

def RecognizeFaces():
    new_window = Toplevel(root)
    new_window.geometry('350x200')
    new_window.config(bg="#88cffa")
    new_window.title('Recognize ')
    lbl = Label(new_window, text="Enter Pin -", bg='#88cffa', font=('times new roman', 10, 'bold'))
    lbl.pack(padx=10, pady=5)
    ent = Entry(new_window, font=('times new roman', 12, 'bold'), textvariable=Id)
    ent.pack(padx=10, pady=5)

    close_btn = Button(new_window, text="Submit", command=check, bg='#88cffa', font=('times new roman', 10, 'bold'))
    close_btn.pack(side=RIGHT,padx=60, pady=40)
    close_btn = Button(new_window, text="Close Me", command=lambda: new_window.destroy(), bg='#88cffa',
                       font=('times new roman', 10, 'bold'))
    close_btn.pack(side=RIGHT, padx=60, pady=40)

def submit():
    pin = Id.get()
    name = Name.get()
    email = Email.get()
    Id.set("")
    Name.set("")
    Email.set("")
    if len(pin) == 4 and name != "" and email!= "":
        Capture_Image.takeImages(pin, name, email)
        #tkinter.messagebox.showinfo("Registration", "Successfully Done!")
    else:
        tkinter.messagebox.showerror("Registration", "Enter correct details")

def check():
    pin = Id.get()
    Id.set("")
    if len(pin) == 4:
        Recognize.recognize_attendence(pin)
        #tkinter.messagebox.showinfo("Recognize", "Successfully Done!")
    else:
        tkinter.messagebox.showerror("Recognize", "Enter correct details")


root = Tk()
lbl = Label(root, text="ICICI Bank ATM", font=('times new roman', 35, 'bold'), bg="#88cffa")
lbl.pack(padx=20, pady=20)
camera = Button(root, text="Check Camera", command=checkCamera, bg='#88cffa', font=('times new roman', 10, 'bold'))
camera.pack(padx=20, pady=20)
register = Button(root, text="Capture Faces", command=CaptureFaces, bg='#88cffa', font=('times new roman', 10, 'bold'))
register.pack(padx=20, pady=20)
train = Button(root, text="Train Images", command=Trainimages, bg='#88cffa', font=('times new roman', 10, 'bold'))
train.pack(padx=20, pady=20)
recognize = Button(root, text="Recognize Faces", command=RecognizeFaces, bg='#88cffa', font=('times new roman', 10, 'bold'))
recognize.pack(padx=20, pady=20)
close_btn = Button(root, text="Close Me", command=lambda : root.destroy(), bg='#88cffa', font=('times new roman', 10, 'bold'))
close_btn.pack(padx=20, pady=20)

Name = StringVar()
Id = StringVar()
Email = StringVar()

root.geometry('500x500')
root.title('Wel-Come to ICICI ATM')
root.config(bg="#88cffa")
root.mainloop()
