#-------- encoding: utf-8 --------
'''
@File    :   LoadBank.py
@Time    :   2022/11/07 22:23:35
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------


from tkinter import *
from tkinter import filedialog
import config

def open_question():
    file_path = filedialog.askopenfilename(title = '打开题库文件', filetypes = [('文本文档', '.txt')])
    config.set_quesiton_path(file_path)
    print(config.get_question_path())
