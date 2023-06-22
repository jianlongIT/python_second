# -*- coding: utf-8 -*-
# Auther : jianlong
import random

from school.course import Course
from school.student import Student
from school.teacher import Teacher


def introduction(str):
    first_title = '******' + str + '学生信息' + '** ** **'
    is_student = create_student()
    c_t = course_to_teacher()
    second_title = '******' + str + '选课结果' + '** ** **'
    for i in range(len(is_student)):
        if i == 0:
            print(first_title)
        is_student[i].add_course(c_t[len(is_student) - 1 - i])
        if i == 2:
            is_student[i].add_course(c_t[3])
        print(is_student[i].str())
    print(second_title)
    for k in range(len(is_student)):
        print(is_student[k].course_detail())


def prepare_course():
    course_infos = []
    courses = {}
    courses['01'] = '网络爬虫'
    courses['02'] = '数据分析'
    courses['03'] = '人工智能'
    courses['04'] = '机器学习'
    courses['05'] = '云计算'
    courses['06'] = '大数据'
    courses['07'] = '图像识别'
    courses['08'] = 'Web开发'
    for k, w in courses:
        course_i = Course(k, w)
        course_infos.append(course_i)
    return course_infos


def create_teacher():
    teachers = []
    str_out = str('T1, 张亮, 13301122001\n' +
                  'T2, 王朋, 13301122002\n' +
                  'T3, 李旭, 13301122003\n' +
                  'T4, 黄国发, 13301122004\n' +
                  'T5, 周勤, 13301122005\n' +
                  'T6, 谢富顺, 13301122006\n' +
                  'T7, 贾教师, 13301122007\n' +
                  'T8, 杨教师, 13301122008\n')
    strs = str_out.split('\n')
    for s in strs:
        str_in = s.split(', ')
        if len(str_in) == 3:
            teacher = Teacher(str_in[0], str_in[1], str_in[2])
            teachers.append(teacher)
    return list(teachers)


def create_student():
    students = []
    s_str = "小亮, 小明, 李红, 小丽, Jone, 小彤, 小K, 慕慕".split(', ')
    for i in range(len(s_str)):
        no = random.randint(1000, 1007)
        name = s_str[i]
        student = Student(no, name)
        students.append(student)
    return students


def course_to_teacher():
    lists = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for i in range(len(ls_course)):
        ls_course[i].binding(ls_teacher[i])
        lists.append(ls_course[i])
    return lists
