import json
import time
import math

students=[{'studentId':'1234456','name':'Bob Vance'}]
classes=[]

def student_with_id(_, info, _name):
    for s in students:
        if students['name'] == _name:
             return s

def class_with_id(_, info, _name):
    for c in classes:
        if classes['name'] == _name:
             return c

def resolver_createStudent(_,info,_name):
    new_student={}
    new_student['studentId']=get_new_id()  
    new_student['name'] = _name
    students.append(new_student)
    print(students)
    return students

def resolver_createClass(_,info,_name):
    new_class={}
    new_class['classId']=get_new_id()  
    new_class['name'] = _name
    classes.append(new_class)
    print(students)
    return students

def get_new_id():
    new_id=int(time.time())
    new_id=math.trunc(new_id)
    return new_id    