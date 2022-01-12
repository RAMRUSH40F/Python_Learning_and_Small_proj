
import tkinter as tk
win = tk.Tk()
win.title('Мое первое графическое окно') # название сверху

#Размеры и геометрия
win.geometry('500x600+200+100') #размеры + отсутпы для запуска
win.resizable(True,True) # возможность изменять размеры по ширине/длине
win.minsize(300,400)
win.maxsize(700,800)

photo = tk.PhotoImage(file='icon_corner.png') # иконка в углу
win.iconphoto(False, photo)

win.config(bg = '#2DFF00')  #  много параметров, один из которых - цвет фона

#entry виджет
 



def get_entry():
	value = name.get()
	if value:
		print(value)
	else:
		print('Empty Entry')

def Delete_symbols():
	name.delete(0, 'end')

def submit():
	print('Имя пользователя:',name.get())
	print('Пароль пользователя: ',password.get())
	Delete_symbols()
	password.delete(0,tk.END)

name = tk.Entry(win) # объясвляем переменную
name.grid(row = 0, column = 1)

password = tk.Entry(win,show = '*')
password.grid(row = 1, column =1)



tk.Button(win,text ='Get', command = get_entry).grid(row= 2,column =0,stick = 'ew')
tk.Button(win,text ='Delete', command = Delete_symbols).grid(row= 2,column =1,stick = 'ew')
tk.Button(win,text ='Вывести 555', command = lambda: name.insert(0,'555'))\
.grid(row= 2,column =2,stick = 'ew') # позиция, текст # можно очищать перед вставкой
tk.Button(win,text ='Submit', command = submit).grid(row= 3,column =0)



tk.Label(win,text = 'Имя').grid(row=0,column = 0, stick = 'we')
tk.Label(win,text = 'Пароль').grid(row=1,column = 0, stick = 'we')

win.grid_columnconfigure(0,minsize= 100)
win.grid_columnconfigure(1,minsize = 100)
win.mainloop() #режим ожидания, режим ожидания данны