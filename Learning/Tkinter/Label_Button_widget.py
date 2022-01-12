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


# Виджет Label
label_1 = tk.Label(win, text = '''Hello!
World''', bg = 'red', fg ='white', font =('Arial',20,'bold',),padx =20,pady=40,anchor = 'sw', height = 5,width = 7, relief =tk.RAISED, bd =10, justify = tk.RIGHT ) # переменная класса Label # 
label_1.pack() #распологаем 


# Виджет Button
def say_hello():
	print('Here we go again')

def add_label():
	label_x = tk.Label(win, text = 'test button')
	label_x.pack()

def counter():
	global count
	count +=1
	btn4['text']= f'Счетчик:{count}' #btn['параметр'], например label1['bg'] = 'red измененние цветов


btn1 = tk.Button(win,text = 'Hello',
				command = say_hello

				)
btn2 = tk.Button(win,text = 'Add new Label',
				command = add_label

				)
btn3_lambda = tk.Button(win,text = 'Add new Label lambda',
				command = lambda: tk.Label(win, text = 'lambda label').pack()

				)
count = 0
btn4 = tk.Button(win,text =f'Счетчик:{count}',
				command = counter,
				bg = 'red',
				activebackground = 'blue',
				state = tk.NORMAL 
				)


btn1.pack()
btn2.pack()
btn3_lambda.pack()
btn4.pack()






win.mainloop() #режим ожидания, режим ожидания данных



