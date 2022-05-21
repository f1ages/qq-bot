#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import api.api as api
import random

req=['?','xs','qs','乐']

def main(data):
    if str(data['sender']['user_id'])=='787362202':
        num=random.randint(0,3)
        api.reply_msg(data,req[num])