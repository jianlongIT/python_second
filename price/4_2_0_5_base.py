# -*- coding: utf-8 -*-
# Auther : jianlong
import os
import time

from price.common import utils, consts

import json

from price.common.consts import F_LEVEL, S_LEVEL
from price.common.error import UserExistError


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json
        self.check()

    def check(self):
        self.__check_user()
        self.__check_gift()
        self.__init_gifts()

    def __check_user(self):
        utils.check(self.user_json)

    def __check_gift(self):
        utils.check(self.gift_json)

    def __read_users(self, time_to_str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())

        if time_to_str:
            for k, v in data.items():
                v['create_time'] = utils.timestamp_to_string(v['create_time'])
                v['update_time'] = utils.timestamp_to_string(v['update_time'])
                data[k] = v
        return data

    def __write_user(self, **user):
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')
        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []

        users = self.__read_users()

        if user['username'] in users:
            raise UserExistError('username %s is exist' % user['username'])

        users.update(
            {user['username']: user}
        )

        json_users = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_users)

    def __change_role(self, username, role):
        users = self.__read_users()
        if username not in users:
            raise Exception('no username')
        if role not in consts.ROLES:
            raise Exception('role is error ')
        user = users.get(username)
        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user
        self.__change_attr(self.user_json, users)

    def __change_active(self, username):
        users = self.__read_users()
        if username not in users:
            raise Exception('no username')
        user = users.get(username)
        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user
        self.__change_attr(self.user_json, users)

    def __delete_user(self, username):
        users = self.__read_users()
        if username not in users:
            raise Exception('no username')
        users.pop(username)
        self.__change_attr(self.user_json, users)

    @staticmethod
    def __change_attr(path, info):
        json_str = json.dumps(info)
        with open(path, 'w') as f:
            f.write(json_str)
        return True

    def __read_gifts(self):
        with open(self.gift_json, 'r') as f:
            data = json.loads(f.read())
        return data

    def __init_gifts(self):
        data = {
            'level1': {
                'level1': {},
                'level2': {},
                'level3': {},

            }, 'level2': {
                'level1': {},
                'level2': {},
                'level3': {},

            }, 'level3': {
                'level1': {},
                'level2': {},
                'level3': {},

            }, 'level4': {
                'level1': {},
                'level2': {},
                'level3': {},

            }}
        read_data = self.__read_gifts()
        if len(read_data) != 0:
            return
        with open(self.gift_json, 'w')as f:
            f.write(json.dumps(data))

    def __write_level(self, first_level, second_level, name, count):
        gifts = self.__gift_check(first_level, second_level)
        gift_pool = gifts[first_level]
        second_gift_pool = gift_pool[second_level]
        if count == 0:
            count = 1
        if name in second_gift_pool:
            current_count = int(second_gift_pool[name]['count'])
            current_count += int(count)
            second_gift_pool[name]['count'] = current_count
        else:
            second_gift_pool[name] = {
                'name': name,
                'count': count
            }
        gift_pool[second_level] = second_gift_pool
        gifts[first_level] = gift_pool
        self.__change_attr(self.gift_json, gifts)

    def __gift_check(self, first_level, second_level):
        if first_level not in F_LEVEL:
            raise Exception('first_level is undefined')
        if second_level not in S_LEVEL:
            raise Exception('second_level is undefined')
        gifts = self.__read_gifts()
        return gifts

    def __gift_update(self, first_level, second_level, name, count=1, is_admin=False):
        assert isinstance(count, int), 'gift count is int'
        gifts = self.__gift_check(first_level, second_level)
        current_count = int(gifts[first_level][second_level][name]['count'])
        if is_admin:
            if count <= 0:
                raise Exception('gift count is error')
            current_count = count
        else:
            if current_count < int(count):
                raise Exception('gift count is error')
            current_count -= int(count)
        gifts[first_level][second_level][name]['count'] = current_count
        self.__change_attr(self.gift_json, gifts)

    def __delete_gift(self, first_level, second_level, name):
        gifts = self.__gift_check(first_level, second_level)
        if name in gifts[first_level][second_level]:
            delete_data = gifts[first_level][second_level].pop(name)
            self.__change_attr(self.gift_json, gifts)
        return delete_data


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')

    base = Base(user_path, gift_path)
    base.write_level('level1', 'level3', 'iPad Pro', '4')
    # result = base.delete_gift('level4', 'level3', 'iPad')
    # print(result)
    # result = base.read_gifts()
    # print(result)
    # base.write_user(username='jianlong', role='admin')
    # base.change_role(username='jianlong', role='nomal')
