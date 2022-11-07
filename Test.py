#-------- encoding: utf-8 --------
'''
@File    :   Test.py
@Time    :   2022/11/07 22:24:07
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
answers = []

if_show_answer = 0

def show_next(qs, asw):
    global now
    global questions
    global rank
    global if_show_answer

    size = len(questions)

    if now < size:
        now = now + 1
    elif now == size:
        now = 1

    if_show_answer = 0

    qs.configure(text = questions[rank[now - 1]])
    asw.configure(text = "")

def show_answer(asw):
    global now
    global answers
    global rank

    global if_show_answer

    size = len(answers)

    try:
        if if_show_answer == 0:
            if_show_answer = 1
            asw.configure(text = answers[rank[now - 1]])
    except:
        print("答案和问题数量需要一致")

def self_test():
    global now
    global questions
    global answers
    global rank
    global if_show_answer

    # Initial
    now = 1
    questions = []
    rank = []
    answers = []
    if_show_answer = 0

    tt = Toplevel()

    pixel = PhotoImage(width=1, height=1)
    
    tt.title('刷题')
    tt.geometry('800x600')
    tt.iconbitmap('./logo.ico')

    question_path = config.get_question_path()
    answer_path = config.get_answer_path()

    # Check if the file_path is empty
    if question_path != None:
        with open(question_path, 'r', encoding = 'utf-8') as f0:
            questions = f0.readlines()
    if answer_path != None:
        with open(answer_path, 'r', encoding = 'utf-8') as f1:
            answers = f1.readlines()
    # Check if the question file is empty
    if questions == []:
        questions = ["文件为空"]
        rank = [0]
    else:
        question_size = len(questions)
        rank_init = [i for i in range(question_size)]
        md = config.get_mode()
        if md == 0:
            rank = rank_init
        elif md == 1:
            rank = random.sample(rank_init, question_size)
    
    # Check if the answer question file is empty
    if answers == []:
        answers = ["文件为空"]
        rank = [0]

    qs = Label(tt, text = questions[rank[now - 1]], font = ("微软雅黑", 12, "bold"), image = pixel, anchor='w', wraplength = 600, justify='left', height = 80, width = 600, compound = "c")
    qs.place(x = 100, y = 100)

    asw = Label(tt, text = "", font = ("圆体", 12, "bold"), image = pixel, anchor='w', wraplength = 600, justify='left', height = 80, width = 600, compound = "c")
    asw.place(x = 100, y = 300)

    bt1 = Button(tt, text = '下一题', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 20, width = 80, compound = "c", command = lambda:show_next(qs, asw))
    bt1.place(x = 260, y = 400)

    bt2 = Button(tt, text = '答案', activeforeground = "white", activebackground = "black", font = ("微软雅黑", 16), image = pixel, height = 20, width = 80, compound = "c", command = lambda:show_answer(asw))
    bt2.place(x = 460, y = 400)

    tt.mainloop()
