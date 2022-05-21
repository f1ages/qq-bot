import api.sql as sql
import api.api as api

def main(data,admin=0):
    res=sql.valiable_m_check(admin)
    msg='moudle:\n'
    if admin ==1:
        for i in res:
            if i[2]==1:
                flag='activated'
            else:
                flag='deactivated'
            msg=msg+str(i[0])+'、'+i[1]+'\t'+i[4]+'\t'+flag+'\n'
    else:
        for i in res:
            if i[2]==1:
                flag='activated'
            else:
                flag='deactivated'
            msg=msg+str(i[0])+'、'+i[1]+' '+flag+'\n'
    api.reply_msg(data,msg)

def usage(data,admin='0'):
    res=sql.using_m_check(admin)
    msg='activated:\n'

    for i in res:
        msg=msg+str(i[0])+'、'+str(i[1])+'\t关键词: '+str(i[5])+'\n'
    api.reply_msg(data,msg)
