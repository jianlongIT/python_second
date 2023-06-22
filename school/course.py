# -*- coding: utf-8 -*-
# Auther : jianlong
import json


class Course(object):
    def __init__(self, no, name, teacher=None):
        self.no = no
        self.name = name
        self.teacher = teacher

    def binding(self, teacher):
        if teacher is not None and teacher.no != '':
            self.teacher = teacher
        else:
            return None

    def str(self):
        course_dect = {'课程名称': self.name, '教师名称': self.teacher.name}
        return course_dect
