import json
import time
import math

students = dict({"1": "Sachin Tendulkar", "2": "Dravid"})
classs=dict({})

def student_with_id(_,info, studentId):
    new_student={}
    new_student['studentId']=studentId
    new_student['name']=students[studentId]
    return new_student

def class_with_id(_,info,classId):
    new_class={}
    new_class['classId']=classId
    new_class['name']=classs[classId]
    return new_class

def resolver_createStudent(_,info, studentName):
    print("here test")
    new_student={}
    new_student['studentId']=get_new_id()
    new_student['name'] = studentName
    students[new_student['studentId']]=studentName
    return new_student

def resolver_createClass(_,info,className):
    new_class={}
    new_class['classId']=get_new_id()
    new_class['name']=className
    classs[new_class['classId']]=className
    return new_class

def resolver_add_student_to_class(_,info,classId,studentId):
    index=-1
    curr_class={}
    for i in range(0,len(students)):
        if (students[i]).get('studentId')==studentId:
            index=i
            break
    if index==-1:
        print('No student with the id')
    else:   
        for i in range(0,len(classs)):
            if (classs[i]).get('classId')==classId:
                (classs[i]).get('students').append(students[index])
                curr_class=classs[i]
                break       
    return  curr_class         
           

def get_new_id():
    new_id=int(time.time())
    new_id=math.trunc(new_id)
    return str(new_id)