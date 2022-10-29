#-------- encoding: utf-8 --------
'''
@File    :   LoadBase.py
@Time    :   2022/10/29 21:53:52
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------

from tkinter import *
from tkinter import filedialog
import config

def open():
    file_path = filedialog.askopenfilename(title = '打开题库文件', filetypes = [('文本文档', '.txt')])
    config.set_path(file_path)
    print(config.get_path())
