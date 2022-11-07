#-------- encoding: utf-8 --------
'''
@File    :   main.py
@Time    :   2022/11/07 22:23:41
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------


from tkinter import *
from LoadBank import *
from LoadAnswer import *
from Test import *
from Mode import *
import config

if __name__ == "__main__":
    config._init()
    
    main_screen = Tk()

    pixel = PhotoImage(width=1, height=1)
    
    main_screen.title('通用题库机')
    main_screen.geometry('800x600')
    main_screen.iconbitmap('./logo.ico')

    main_title = Label(main_screen, text = '刷题机', font = ("楷体", 48, "bold"))
    main_title.place(x = 314, y = 20)


    bt1 = Button(main_screen, text = '载入题库', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 40, width = 100, compound = "c", command = lambda:open_question())
    bt1.place(x = 350, y = 150)
    
    bt2 = Button(main_screen, text = '载入答案', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 40, width = 100, compound = "c", command = lambda:open_answer())
    bt2.place(x = 350, y = 250)

    bt3 = Button(main_screen, text = '模式', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 40, width = 100, compound = "c", command = lambda:select_mode())
    bt3.place(x = 350, y = 350)

    bt4 = Button(main_screen, text = '开始刷题', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 40, width = 100, compound = "c", command = lambda:self_test())
    bt4.place(x = 350, y = 450)

    main_screen.mainloop()