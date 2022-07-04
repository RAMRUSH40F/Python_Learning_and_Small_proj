
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



#Виджет grid() - помогает распологать виджеты в виде таблицы
win.grid_columnconfigure(0,minsize= 200)
win.grid_columnconfigure(1,minsize = 100)

btn1 = tk.Button(win, text = 'hello 1')
btn2 = tk.Button(win, text = 'hello 2')
btn3 = tk.Button(win, text = 'hello 3')
btn4 = tk.Button(win, text = 'hello 4 not equal')
btn5 = tk.Button(win, text = 'hello 5')
btn6 = tk.Button(win, text = 'hello 6')
btn7 = tk.Button(win, text = 'hello 7')
btn8 = tk.Button(win, text = 'hello 8')

btn1.grid(row = 0,column =0,stick ='we')
btn2.grid(row = 0,column =1, stick = 'ew')
btn3.grid(row = 1,column =0, stick ='we')
btn4.grid(row = 1,column =1)
btn5.grid(row = 2,column =0,)
btn6.grid(row = 2,column =1, stick = 'we')
btn7.grid(row = 3,column =0,columnspan = 2,stick ='we') #span -занять площадь, stick -растянуть по сторонам света
btn8.grid(row = 0, column = 2, rowspan = 4, stick = 'ns') 


#for i in range(5):
#	for j in range(2):    
#		tk.Button(win, text =f'Строка{i},колонка {j}').grid(row = i, column = j)
#
win.mainloop() #режим ожидания, режим ожидания данны