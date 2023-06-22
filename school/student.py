# -*- coding: utf-8 -*-
# Auther : jianlong
class Student(object):
    def __init__(self, s_number='', name='', courses=[]):
        self.s_number = s_number
        self.name = name
        self.courses = courses

    def course_detail(self):
        return 'Name:{} Selected:{}'.format(self.name, self.courses[0].str())

    def add_course(self, cour_info):
        ss = [cour_info]
        self.courses = ss

    def str(self):
        return 'name:{},s_number:{}'.format(self.name, self.s_number)
