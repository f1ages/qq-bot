
import api.sql as sql
import api.api as api
import plugins.ddl.cron_control as cron_control

def main(data):
    u_id=str(data['sender']['user_id'])
    msg='ddl list:\n'
    cnt=1

    res=sql.get_user_ddl(u_id)
    for i in res:
        msg=msg+str(cnt)+'、'+str(i[3])+' '+str(i[2])+'\t'+i[1]+'\treal id:'+str(i[0])+'\n'
        cnt+=1

    api.reply_msg(data,msg)

def del_ddl(data):
    id=str(data['message'][8:])
    try:
        sql.del_ddl_by_id(id)
        cron_control.del_(id)
        api.reply_msg(data,'success')
    except:
        api.reply_msg(data,'err')
        return False