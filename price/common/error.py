# -*- coding: utf-8 -*-
# Auther : jianlong
class NotPathError(Exception):
    def __init__(self, message='path is undefined'):
        self.message = message


class FileFormatError(Exception):
    def __init__(self, message='is not json file'):
        self.message = message


class NotFileError(Exception):
    def __init__(self, message='file is undefined'):
        self.message = message


class UserExistError(Exception):
    def __init__(self, message):
        self.message = message
