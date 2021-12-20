import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('Камила') # название сверху

#формируем размеры кнопок
win.geometry('250x315+300+300')
win.resizable(False,False)

def column_figure(i):
	return win.grid_columnconfigure(i,minsize= 60)

def row_figure(i):
	return win.grid_rowconfigure(i,minsize = 60)

column_figure(0);column_figure(1);column_figure(2);column_figure(3);column_figure(4);
row_figure(0);row_figure(1);row_figure(2);row_figure(3);row_figure(4)





photo = tk.PhotoImage(file='icon_corner.png') # иконка в углу
win.iconphoto(False, photo)

win.config(bg = '#FFBCD9')

# функции кнопок 
def insert_num(i):
	value['state'] = tk.NORMAL
	memory = value.get()
	if memory == '0':
		memory = memory[1:]
	memory = memory + str(i)
	value.delete(0,tk.END)
	value.insert(0,memory)
	value['state'] = tk.DISABLED

def insert_operation(operation):
	value['state'] = tk.NORMAL
	memory = value.get()
	if memory[-1] in '+-/*':
		memory = memory[:-1]
	memory = memory + str(operation)
	value.delete(0,tk.END)
	value.insert(0,memory)
	value['state'] = tk.DISABLED

def calculate():
	value['state'] = tk.NORMAL
	memory = value.get()
	if memory[-1] in '+-/*':
		memory = memory + memory[:-1]
	value.delete(0,tk.END)

	try:
		value.insert(0,eval(memory))
	except (NameError, SyntaxError):
		messagebox.showinfo('Внимание','Вы ввели символы')
	except ZeroDivisionError:
		messagebox.showinfo('Внимание!','На ноль делить НЕЛЬЗЯ!')

	value['state'] = tk.DISABLED
#созданеи кнопок и entry


value = tk.Entry(win, justify = tk.RIGHT, font = ('Arial', 15,), width = 15) 
value.insert(0,'0')
value['state'] = tk.DISABLED
value.grid(row = 0,column = 0, stick = 'ew',columnspan = 4, padx= 15)

def make_buton_num(i):
	return tk.Button(win,text = i, command = lambda : insert_num(i), bd =5,font = ('Arial', 16))

def make_operation_button(operation):
	return tk.Button(win, text = operation, command = lambda: insert_operation(operation), bd = 5, font = ('Arial', 17), fg = '#fa529e')

def clear():
	value['state'] = tk.NORMAL
	value.delete(0,tk.END)
	value.insert(0, '0')
	value['state'] = tk.DISABLED
make_buton_num(1).grid(row = 1,column=0,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(2).grid(row = 1,column=1,stick = 'sewn',padx = 5, pady = 5)
make_buton_num(3).grid(row = 1,column=2,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(4).grid(row = 2,column=0,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(5).grid(row = 2,column=1,stick = 'snew',padx = 5, pady = 5)
make_buton_num(6).grid(row = 2,column=2,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(7).grid(row = 3,column=0,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(8).grid(row = 3,column=1,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(9).grid(row = 3,column=2,stick = 'ewsn',padx = 5, pady = 5)
make_buton_num(0).grid(row = 4,column=0,stick = 'ewns',padx = 5, pady = 5)

tk.Button(win,text = 'Очистить', command = clear , bd = 5, font = ('Arial', 7, 'bold'), fg = '#fa529e').grid(row = 4,column=1,stick = 'ewns',padx = 5, pady = 5)



make_operation_button('+').grid(column = 3, row = 2, stick = 'ewsn', padx = 5, pady = 5)
make_operation_button('-').grid(column = 3, row = 1, stick = 'ewsn', padx = 5, pady = 5)
make_operation_button('/').grid(column = 3, row = 3, stick = 'ewsn', padx = 5, pady = 5)
make_operation_button('*').grid(column = 3, row = 4, stick = 'ewsn', padx = 5, pady = 5)

tk.Button(win,text= '=',command = calculate ,bd =5, font = ('Arial', 15), fg = '#fa529e').grid(column = 2, row = 4, stick = 'ewsn', padx = 5, pady = 5)


# обработка нажатие клавиш через bind НОВОЕ !

def press_key(key):
	#print(repr(key.char)) # показ нажатых клавиш в консоли
	if key.char.isdigit():
		insert_num(key.char)

	elif key.char in '+-/*':
		insert_operation(key.char)

	elif key.char == '\r':
		calculate()
	elif key.char == '\x08':
		value['state'] = tk.NORMAL
		memory = value.get()
		memory = memory[:-1]
		value.delete(0,tk.END)
		value.insert(0,memory)
		value['state'] = tk.DISABLED



win.bind('<Key>', press_key)



win.mainloop()
