import json
import time
import math

students = []
classes= []

def student_with_id(_,info, studentId):
    for s in students:
        if s.get('studentId')==studentId:
            return s

def class_with_id(_,info,classId):
    for c in classes:
        if c.get('classId')==classId:
            return c


def resolver_createStudent(_,info, studentName):
    print("here test")
    new_student={}
    new_student['studentId']=get_new_id()
    new_student['studentName'] = studentName
    students.append(new_student)
    return new_student

def resolver_createClass(_,info,className):
    new_class={}
    new_class['classId']=get_new_id()
    new_class['className']=className
    new_class['students']=[]
    classes.append(new_class)
    return new_class

def resolver_add_student_to_class(_,info,classId,studentId):
    index=-1
    for i in range(0,len(students)):
        if (students[i]).get('studentId')==studentId:
            index=i
            break
    if index==-1:
        print('No student with the id')
    else:   
        for i in range(0,len(classes)):
            if (classes[i]).get('classId')==classId:
                (classes[i]).get('students').append(students[index])
                curr_class=classes[i]
                break  
    return curr_class        
           
def get_new_id():
    new_id=int(time.time())
    new_id=math.trunc(new_id)
    return str(new_id)