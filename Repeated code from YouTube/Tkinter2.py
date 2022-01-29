from tkinter import *
import pickle
from tkinter import messagebox 


root = Tk()
root.geometry("300x500")
root.title("Войти в систему")

def registration():
    text = Label(text='Для входа в систему - зарегистрируйтесь')
    text_log = Label(text="Введите ваш логин:")
    global register_login
    register_login = Entry()
    text__password1 = Label(text="Введите ваш пароль:")
    global register__password1
    register__password1 = Entry()
    text_password2 = Label(text="Ещё раз пароль:")
    register_password2 = Entry(show="*")
    button_register = Button(text="Зарегистрироваться!", command=lambda: save())
    text.pack()
    text_log.pack()
    register_login.pack()
    text__password1.pack()
    register__password1.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()


def login():
    text_log = Label(text="Поздравляем! теперь Вы можете войти в систему!")
    text_enter_login = Label(text="Введите Ваш логин:")
    global enter_login
    enter_login = Entry()
    text_enter_pass = Label(text="Введите Ваш пароль:")
    global enter_password 
    enter_password = Entry(show="*")
    button_enter = Button(text="Войти", command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

def save():
    login_pass_save = {}
    login_pass_save[register_login.get()] = register__password1.get()
    f = open("login.txt", "wb")
    pickle.dump(login_pass_save, f)
    f.close()
    login()

def log_pass():
    f = open("login.txt", "rb")
    a = pickle.load(f)
    f.close()
    if enter_login.get() in a:
        if enter_password.get() == a[enter_login.get()]:
            messagebox.showinfo("Вход выполнен", "Привет! у тебя 5 новых сообщений!")
        else:
            messagebox.showerror("Ошибка!", "Вы ввели неверный логин или пароль")   
    else:
        messagebox.showerror("Ошибка!", "Неверный логин!")        

registration()

root.mainloop()