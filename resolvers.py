import json
import time
import math

students = {}
classs= {}

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
    new_class['students']=[]
    classs[new_class['classId']]=new_class
    return new_class

def resolver_add_student_to_class(_,info,classId,studentId):
    curr_class = classs[classId]
    (curr_class['students']).append(studentId)
    return curr_class       
           
def get_new_id():
    new_id=int(time.time())
    new_id=math.trunc(new_id)
    return str(new_id)