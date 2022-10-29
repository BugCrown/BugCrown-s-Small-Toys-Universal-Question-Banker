#-------- encoding: utf-8 --------
'''
@File    :   Mode.py
@Time    :   2022/10/29 21:53:35
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------

from tkinter import *
import config

def change_mode(md: int):
    config.set_mode(md)
    print(md, config.get_mode())

def select_mode():
    mde = Toplevel()

    pixel = PhotoImage(width=1, height=1)
    
    mde.title('模式')
    mde.geometry('400x400')
    mde.iconbitmap('./logo.ico')

    bt1 = Button(mde, text = '顺序', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 20, width = 80, compound = "c", command = lambda:change_mode(0))
    bt1.place(x = 160, y = 100)

    bt2 = Button(mde, text = '乱序', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 20, width = 80, compound = "c", command = lambda:change_mode(1))
    bt2.place(x = 160, y = 300)

    mde.mainloop()