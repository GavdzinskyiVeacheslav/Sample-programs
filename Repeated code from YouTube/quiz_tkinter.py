from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Quiz")
root.geometry('300x300')


def que_one():
    question = Label(root, text="A pear hangs and cannot be eaten?")
    answer = Entry()
    btn = Button(root, text="To answer!", command=lambda: game1(que_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(que_two):
        if answer.get().lower() == 'bulb':
            que_two()
        else:
            messagebox.showerror("Error!", "Try again!")


def que_two():
    question_2 = Label(root, text="In winter and summer the same color?")
    answer_2 = Entry()
    btn_2 = Button(root, text="To answer!", command=lambda: game2(que_two))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game2(que_two):
        if answer_2.get().lower() == 'fir-tree':
            messagebox.showinfo("Victory", "You are great!")
        else:
            messagebox.showerror("Error!", "Try again")


que_one()

root.mainloop()