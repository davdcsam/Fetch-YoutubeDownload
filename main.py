from tkinter import *
from tkinter import messagebox as MessageBox
from pytube import YouTube

def action():
    link = video.get()
    video = YouTube(link)
    download = video.streams.get_highest_resolution()
    download.download()

def popup():
    MessageBox.showinfo("GitHub Creator", "https://github.com/davdcsam")

root = Tk()
root.config(bd=15)
root.title("Fetch YouTube Download")

image = PhotoImage(file="fetch.png") 
foto = Label(root, image=image, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="GitHub", command=popup)
menubar.add_command(label="Exit", command=root.destroy)

instruction = Label(root, text="Paste YouTube link for start download\n")
instruction.grid(row=0, column=1)

video = Entry(root)
video.grid(row=1, column=1)

button = Button(root, text="Download", command=action)
button.grid(row=2, column=1)

root.mainloop()