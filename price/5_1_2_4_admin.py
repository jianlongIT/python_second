# -*- coding: utf-8 -*-
# Auther : jianlong
import os

from price.base import Base


class Admin(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json=user_json, gift_json=gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user is None:
            raise Exception('current_user is none %s' % self.username)
        if current_user.get('active') is False:
            raise Exception('active is  false')
        if current_user.get('role') != 'admin':
            raise Exception('%s is not admin' % current_user.get('username'))
        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')

    def add_user(self, username, role):
        self.get_user()
        if self.role != 'admin':
            raise Exception('is not admin')
        self._Base__write_user(username=username, role=role)

    def __check(self):
        self.get_user()
        if self.role != 'admin':
            raise Exception('is not admin')

    def change_active(self, username):
        self.__check()
        self._Base__change_active(username=username)

    def change_role(self, username, role):
        self.__check()
        self._Base__change_role(username=username, role=role)

    def add_gift(self, first_level, second_level, name, count):
        self.__check()
        self._Base__write_level(first_level=first_level, second_level=second_level, name=name, count=count)

    def delete_gift(self, first_level, second_level, name):
        self.__check()
        self._Base__delete_gift(first_level=first_level, second_level=second_level, name=name)

    def gift_update(self, first_level, second_level, name, count):
        self.__check()
        self._Base__gift_update(first_level=first_level, second_level=second_level, name=name, count=count,
                                is_admin=True)


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    admin = Admin('jianlong', user_path, gift_path)
    admin.change_role('jianlong3', 'normal')
    admin.add_gift(first_level='level1', second_level='level2', name='Mac mini', count=233)
