import api.sql as sql
import api.api as api

def main(data):
    flag=str(data['message'][-1])
    name=data['message'][1:-2]
    id=sql.get_m_id(name)
    if id == False:
        api.reply_msg(data,'no such plugin')
        return
    if flag=='1':
        sql.enable_m(id)
        if sql.is_valiable_m_check(id)==1:
            api.reply_msg(data,'success')
        else:
            api.reply_msg(data,'err, open plugin failed')
    elif flag=='0':
        sql.disable_m(id)
        if sql.is_valiable_m_check(id)==0:
            api.reply_msg(data,'success')
        else:
            api.reply_msg(data,'err, close plugin failed')
    else:
        api.reply_msg(data,'error parameter or format')
