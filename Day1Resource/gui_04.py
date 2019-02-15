import tkinter
import tkinter.messagebox

window = tkinter.Tk()

#set the window's size
window.geometry("300x300")

def displayMsg():
    tkinter.messagebox.showinfo("Hello Python","Hello World!")

#Add a button
button = tkinter.Button(window, text="Start", bg="gray", command=displayMsg)
button.config(font=("Courier", 30))
button.pack(side="top", expand=tkinter.YES)

window.mainloop()





