# -*- coding: utf-8 -*-
# Auther : jianlong
class Teacher(object):
    def __init__(self, no, name, phone_no):
        self.no = no
        self.name = name
        self.phone_no = phone_no

    def str(self):
        return 'name:{},s_number:{}'.format(self.name, self.no)
