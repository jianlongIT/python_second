# -*- coding: utf-8 -*-
# Auther : jianlong
import os
import random

from price.base import Base
from price.common import utils


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()
        self.gift_random = list(range(1, 101))

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user is None:
            raise Exception('get user error there is not user %s' % self.username)

        if current_user.get('role') != 'normal':
            raise Exception('%s is not normal role' % self.username)

        if current_user.get('active') is False:
            raise Exception('%s is not active' % self.username)
        self.user = current_user
        self.username = current_user.get('username')
        self.role = current_user.get('role')
        self.gifts = current_user.get('gifts')
        self.create_time = utils.timestamp_to_string(current_user.get('create_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gift_lift = []
        for key1, value1 in gifts.items():
            for key2, value2 in value1.items():
                for k, v in value2.items():
                    gift_lift.append(v.get('name'))
        return gift_lift

    def choice_gift(self):
        gifts = self._Base__read_gifts()
        level_one_num = random.choice(self.gift_random)
        level_two_num = random.choice(self.gift_random)

        level_first, level_second = None, None
        if level_one_num < 50:
            level_first = 'level1'
        elif 50 < level_one_num < 80:
            level_first = 'level2'
        elif 80 < level_one_num < 94:
            level_first = 'level3'
        else:
            level_first = 'level4'

        if level_two_num < 50:
            level_second = 'level1'
        elif 50 < level_two_num < 80:
            level_second = 'level2'
        else:
            level_second = 'level3'
        gift_info = gifts[level_first][level_second]
        if len(gift_info) == 0:
            print('您没有中奖')
            return
        last_gift_infos = [v for k, v in gift_info.items()]
        last_gift = random.choice(last_gift_infos)
        if last_gift.get('count') == 0:
            print('您没有中奖')
            return
        print('抽中%s' % last_gift.get('name'))
        last_gift['count'] = int(last_gift['count']) - 1
        gifts[level_first][level_second][last_gift.get('name')] = last_gift
        self._Base__change_attr(self.gift_json, gifts)
        self.user['gifts'].append(last_gift['name'])
        self.__update()

    def __update(self):
        users = self._Base__read_users()
        users[self.username] = self.user
        self._Base__change_attr(self.user_json, users)


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user = User('jianlong3', user_path, gift_path)
    user.choice_gift()
