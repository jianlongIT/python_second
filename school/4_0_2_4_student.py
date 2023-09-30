# -*- coding: utf-8 -*-
# Auther : jianlong
import json


class Student(object):
    def __init__(self, s_number='', name='', courses=[]):
        self.s_number = s_number
        self.name = name
        self.courses = courses

    def course_detail(self):
        lists = []
        for s_c in self.courses:
            s_c_str = s_c.str()
            lists.append(s_c_str)

        return 'Name:{} , Selected:{}'.format(self.name, str(lists))

    def add_course(self, cour_info):
        if len(self.courses) == 0:
            ss = [cour_info]
            self.courses = ss
        else:
            self.courses.append(cour_info)

    def str(self):
        return 'name:{},s_number:{}'.format(self.name, self.s_number)
