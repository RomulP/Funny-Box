from tkinter import *

def clicked():
	res = "Привет {}".format(txt.get())
	lbl.configure(text=res)

wnd = Tk()
wnd.title('Шкатулка')
wnd.geometry('500x300')

lbl = Label(wnd, text='Привет', font=('Arial Bold', 20))
lbl.grid(column=0, row=0)  # виджет

txt = Entry(wnd, width=10)
txt.grid(column=1, row=0)  # однострочный ввод

btn = Button(
    wnd,
    text='Не нажимать!',
    bg='black',
    fg='red',
    command=clicked
)
btn.grid(column=2, row=0)  # кнопка

wnd.mainloop()
