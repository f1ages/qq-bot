#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import time

host="http://10.0.24.10:5700/"

def send_private_message(id,text):
    url=host+"send_private_msg?user_id="+id+"&message="+text
    res=requests.get(url)

def send_group_message(id,text):
    url=host+"send_group_msg?group_id="+id+"&message="+text
    res=requests.get(url)

def send_group_forward_msg(id,text):
    url=host+"send_group_forward_msg?group_id"+id+"&message"+text
    res=requests.get(url)

def send_msg(id,text,type='private'):
    if type=='private':
        url=host+"send_private_msg?user_id="+id+"&message="+text
    elif type=='group':
        url=host+"send_group_msg?group_id="+id+"&message="+text
    else:
        return False
    res=requests.get(url)

def reply_msg(data,text):
    if data['message_type']=='private':
        url=host+"send_private_msg?user_id="+str(data['sender']['user_id'])+"&message="+text
    elif data['message_type']=='group':
        url=host+"send_group_msg?group_id="+str(data['group_id'])+"&message="+text
    else:
        return False
    res=requests.get(url)

def delete_msg(id):
    url=host+"delete_msg?message_id="+id
    res=requests.get(url)

def get_msg(id):
    url=host+"get_msg?message_id="+id
    res=requests.get(url)
    return res.text

def get_forward_msg(id):
    url=host+"get_forward_msg?message_id="+id
    res=requests.get(url)
    return res.text

def get_image(id):
    url=host+"get_image?file="+id
    res=requests.get(url)
    return res.text

def group_kick(g_id,u_id,reject_add_req='false'):
    url=host+"set_group_kick?group_id="+g_id+"&user_id="+u_id+"&reject_add_request="+reject_add_req
    res=requests.get(url)

def group_ban(g_id,u_id,times='60'):
    url=host+"set_group_ban?group_id="+g_id+"&user_id="+u_id+"&duration="+times
    res=requests.get(url)

def group_unban(g_id,u_id):
    url=host+"set_group_ban?group_id="+g_id+"&user_id="+u_id+"&duration=0"
    res=requests.get(url)

def group_anonymous_ban(g_id,u_id,u_flag,times='60'):
    url=host+"set_group_anonymous_ban?group_id="+g_id+"&anoymous="+u_id+"&flag="+u_flag+"&duration="+times
    res=requests.get(url)

def group_whole_ban(id):
    url=host+"set_group_whole_ban?group_id="+id+"&enable=true"
    res=requests.get(url)

def group_whole_unban(id):
    url=host+"set_group_whole_ban?group_id="+id+"&enable=false"
    res=requests.get(url)

def set_group_admin(g_id,u_id,flag='true'):
    url=host+"set_group_admin?group_id="+g_id+"&user_id="+u_id+"&enalbe="+flag
    res=requests.get(url)

def set_group_anonymous(g_id,flag):
    url=host+"set_group_anonymous?group_id="+g_id+"&enable="+flag
    res=requests.get(url)

def set_group_card(g_id,u_id,card=''):
    url=host+"set_group_card?group_id="+g_id+"&user_id="+u_id+'&card='+card
    res=requests.get(url)

def set_goup_name(g_id,name):
    url=host+"set_group_name?group_id="+g_id+"&group_name="+name
    res=requests.get(url)

def leave_group(g_id,flag):
    url=host+"set_group_leave?set_group_leave?group_id="+g_id+"is_dismiss="+flag
    res=requests.get(url)

def set_group_special_title(g_id,u_id,title='',times=-1):
    url='set_group_special_title?group_id='+g_id+'&user_id'+u_id+'&special_title='+title
    if times == -1:
        res=requests.get(url)
        return
    else:
        res=requests.get(url)
        time.sleep(times)
        url='set_group_special_title?group_id='+g_id+'&user_id'+u_id+'&special_title='
        res=requests.get(url)
        return

def friend_add_req(flag,approve='true',remark=''):
    url=host+'set_friend_add_request?flag='+flag+'&approve='+approve+'&remark='+remark
    res=requests.get(url)

def set_group_add(flag,type,approve='true',reason=''):
    url=host+'set_group_add_request?flag='+flag+'&type='+type+'&approve='+approve+'&reason='+reason
    res=requests.get(url)

def friend_list():
    url=host+"get_friend_list"
    res=requests.get(url)
    return res.text

def delete_friend(id):
    url=host+'delete_friend?friend_id='+id
    res=requests.get(url)

def can_send_img_check():
    url=host+'can_send_image'
    res=requests.get(url)
    return res.text

def can_send_rec_check():
    url=host+'can_send_record'
    res=requests.get(url)
    return res.text

def restart_cqhttp():
    url=host+'set_restart'
    res=requests.get(url)

def set_essence_msg(id):
    url=host+'set_essence_msg?message_id='+id
    res=requests.get(url)

def delete_essence_msg(id):
    url=host+'delete_essence_msg?message_id='+id
    res=requests.get(url)