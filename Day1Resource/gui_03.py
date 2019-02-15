import tkinter

window = tkinter.Tk()

#set the window's size
window.geometry("300x300")

#Add a button
button = tkinter.Button(window, text="Start", bg="gray")
button.config(font=("Courier", 30))
button.pack(side="top", expand=tkinter.YES)

window.mainloop()



