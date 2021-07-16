import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter.messagebox import showerror
from tkinter import messagebox
import codecs

APP_NAME = 'text_edit'
WIDTH = 700
HEIGHT = 400

WIDTH_TEXT = 350
HEIGHT_TEXT = 200

window = tkinter.Tk()
window.title(APP_NAME)
window.minsize(width=WIDTH, height=HEIGHT)
window.maxsize(width=WIDTH, height=HEIGHT)

class Function:
    def __init__(self):
        self.file_name = tkinter.NONE
    
    def add_new_file(self):
        self.file_name = 'not_name'
        text.delete('1.0', tkinter.END)
    
    def save_file(self):
        info = text.get('1.0', tkinter.END)
        codecs.encode(info, encoding='utf-8')
        file = open(self.file_name, 'w')
        file.write(info)
        file.close()

    def quit(self):
        window.destroy()

    def open_file(self):   #Работает только с txt
        choose_file = askopenfile(mode='r')
        path = choose_file.read()
        text.delete('1.0', tkinter.END)
        text.insert('1.0', path)
    def save_file_as(self):
        file = tkinter.filedialog.asksaveasfilename(defaultextension='txt')
        info = text.get('1.0', tkinter.END)
        codecs.encode(info, encoding='utf-8')
        try:
            file = open(file, 'w')
            file.write(info)
            file.close()
        except:
            print(title='Ошибка')
        
    def print_info(self):
        messagebox.showinfo('Справка', 'Это справка. Данная программа представляет собой текстовый редактор, в котором вы можете редактировать текст')



text = tkinter.Text(window, width=200, height=200, wrap='word')
scroll_x = Scrollbar(window, orient=HORIZONTAL, command=XView())
scroll_y = Scrollbar(window, orient=VERTICAL, command=YView())
scroll_x.pack(side='bottom', fill='x')
scroll_y.pack(side='right', fill='y')
text.configure(xscrollcommand=scroll_x.set)
text.configure(yscrollcommand=scroll_y.set)
text.pack()

canv = Canvas(window, width=WIDTH, height=HEIGHT)
canv.pack()

function = Function()
menu = tkinter.Menu(window)
file_menu = tkinter.Menu(menu, bg='gray22')
file_menu.add_command(label='Новый файл', command=function.add_new_file)
file_menu.add_command(label='Открыть', command=function.open_file)
file_menu.add_separator()
file_menu.add_command(label='Сохранить', command=function.save_file)
file_menu.add_command(label='Сохранить как', command=function.save_file_as)

edit_menu = tkinter.Menu(window)
edit_menu.add_command(label='Вырезать')
edit_menu.add_command(label='Копировать')
edit_menu.add_command(label='Вставить')

reference_menu = tkinter.Menu(menu)
reference_menu.add_command(label='Документация', command=function.print_info)
reference_menu.add_command(label='Поиск запросов функций')

exit_menu = tkinter.Menu(menu)
exit_menu.add_command(label='Выйти', command=function.quit)

menu.add_cascade(label='Файл', menu=file_menu)
menu.add_cascade(label='Правка', menu=edit_menu)
menu.add_cascade(label='Справка', menu=reference_menu)
menu.add_cascade(label='Выход', menu=exit_menu)

window.configure(menu=menu)

window.mainloop()