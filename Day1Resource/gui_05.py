import tkinter
import tkinter.messagebox

window = tkinter.Tk()

#set the window's size
window.geometry("300x300")

def show_answer():
    Ans = int(num1.get()) + int(num2.get())
    print(Ans)
    ans.insert(0,Ans) 

label1 = tkinter.Label(window, text = "Enter Num 1:").grid(row=0)
label2 = tkinter.Label(window, text = "Enter Num 2:").grid(row=1)
label3 = tkinter.Label(window, text = "The Sum is:").grid(row=2)

num1 = tkinter.Entry(window)
num2 = tkinter.Entry(window)
ans = tkinter.Entry(window)

num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
ans.grid(row=2, column=1)

#Add a button
button1 = tkinter.Button(window, text="Show", bg="gray", command=show_answer)
button1.grid(row=4, column=0)

window.mainloop()

