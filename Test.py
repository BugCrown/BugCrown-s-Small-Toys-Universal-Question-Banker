#-------- encoding: utf-8 --------
'''
@File    :   test.py
@Time    :   2022/10/29 21:53:17
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------

from tkinter import *
import config
import random

now = 1
questions = []
rank = []

def show_next(qs):
    global now
    global questions
    global rank
    
    size = len(questions)

    if now < size:
        now = now + 1
    elif now == size:
        now = 1

    qs.configure(text = questions[rank[now - 1]])

def self_test():
    global now
    global questions
    global rank

    tt = Toplevel()

    pixel = PhotoImage(width=1, height=1)
    
    tt.title('刷题')
    tt.geometry('800x600')
    tt.iconbitmap('./logo.ico')

    file_path = config.get_path()

    # Check if the file_path is empty
    if file_path != None:
        with open(file_path, 'r', encoding = 'utf-8') as f:
            questions = f.readlines()

    # Check if the file is empty
    if questions == []:
        questions = ["文件为空"]
        rank = [0]
    else:
        size = len(questions)
        rank_init = [i for i in range(size)]
        md = config.get_mode()
        if md == 0:
            rank = rank_init
        elif md == 1:
            rank = random.sample(rank_init, size)
    
    qs = Label(tt, text = questions[rank[now - 1]], font = ("微软雅黑", 12, "bold"), image = pixel, anchor='w', wraplength = 600, justify='left', height = 80, width = 600, compound = "c")
    qs.place(x = 100, y = 100)

    bt1 = Button(tt, text = '下一题', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 20, width = 80, compound = "c", command = lambda:show_next(qs))
    bt1.place(x = 360, y = 400)

    tt.mainloop()
