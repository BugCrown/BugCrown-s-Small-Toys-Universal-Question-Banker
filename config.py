from email.header import Header


#-------- encoding: utf-8 --------
'''
@File    :   config.py
@Time    :   2022/10/29 21:50:55
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------

# Global value: file_path
# Global value: mode 0: order 1: random
def _init():
    global file_path
    global mode
    file_path = ''
    mode = 0

def set_path(path: str):
    global file_path
    file_path = path

def get_path():
    return file_path

def set_mode(md: int):
    global mode
    mode = md

def get_mode():
    return mode