#-------- encoding: utf-8 --------
'''
@File    :   config.py
@Time    :   2022/11/07 22:23:25
@Author  :   BugCrown 
@Version :   Demo
@Contact :   grantbugcrown@gmail.com
'''
#---------------------------------


# Global value: question_path
# Global value: answer_path
# Global value: mode 0: order 1: random
def _init():
    global question_path
    global answer_path
    global mode
    question_path = ''
    answer_path = ''
    mode = 0

def set_quesiton_path(path: str):
    global question_path
    question_path = path

def get_question_path():
    return question_path

def set_answer_path(path: str):
    global answer_path
    answer_path = path

def get_answer_path():
    return answer_path
    
def set_mode(md: int):
    global mode
    mode = md

def get_mode():
    return mode