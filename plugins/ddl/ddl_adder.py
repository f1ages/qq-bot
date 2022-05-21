import api.sql as sql
import api.api as api
import plugins.ddl.cron_control as cron_control
import time as times

def main(data):
    msg=data['message']
    r_msg=['','','','','']
    time=['','','','','','','','','','']
    pre=0
    cnt=0
    pret=0
    cntt=0
    u_id=data['sender']['user_id']

    for i in range(len(msg)):
        if msg[i] == ';' or msg[i]=='；':
            r_msg[cnt]=msg[pre:i]
            cnt+=1
            pre=i+1
    remind_time_or_msg=msg[pre:]
    for i in range(2):
        i+=1
        for j in range(len(r_msg[i])):
            if r_msg[i][j]=='-' or r_msg[i][j]==':' or r_msg[i][j]=='：':
                time[cntt]=str(r_msg[i][pret:j])
                cntt+=1
                pret=j+1
        time[cntt]=r_msg[i][pret:]
        pret=0
        cntt+=1

    if cntt != 5 or cnt < 3 or cnt > 4:
        api.reply_msg(data,'error,wrong parmater')
        return
    #time_text=

    if cnt ==4 and remind_time_or_msg.isdigit()==False:
        api.reply_msg(data,'error,wrong parmater')
        return

    for i in range(5):
        #print(i)
        if time[i].isdigit()==False:
            api.reply_msg(data,'error,wrong parmater')
            return

    if remind_time_or_msg.isdigit():
        if int(remind_time_or_msg) > 1440 or int(remind_time_or_msg) < 0:
            api.reply_msg(data,'error,wrong parmater')
            return

    time_sum=int(time[3])*60+int(time[4])
    if remind_time_or_msg.isdigit():
        if time_sum>int(remind_time_or_msg):
            real_time=time_sum-int(remind_time_or_msg)
            real_h=real_time//60
            real_min=real_time%60
            real_day=int(time[2])
        else:
            real_time=time_sum-int(remind_time_or_msg)+1440
            real_h=real_time//60
            real_min=real_time%60
            real_day=int(time[2])-1
    else:
        real_day=int(time[2])
        real_h=int(time[3])-1
        real_min=int(time[4])

    time_now=times.strftime('%Y-%m-%d %H:%M',times.localtime())
    time_ins=time[0]+'-'+time[1]+'-'+str(real_day)+' '+str(real_h)+':'+str(real_min)
    time_ins_t=times.strptime(time_ins,'%Y-%m-%d %H:%M')
    time_now_t=times.strptime(time_now,'%Y-%m-%d %H:%M')
    if (time_now_t>time_ins_t):
        api.reply_msg(data,'error,remind time must be greater than now');
        return

    date=''+str(time[0])

    if int(time[1]) < 10:
        date=date+'-0'+str(time[1])
        #print(date)
    else:
        date=date+'-'+str(time[1])
    if int(time[2]) < 10:
        date=date+'-0'+str(time[2])
    else:
        date=date+'-'+str(time[2])

    if remind_time_or_msg.isdigit():
        id=sql.get_id_by_msg(r_msg[3])
        if id:
            for i in range(len(id)):
                res=sql.get_ddl_by_id(id[i][0])
                if str(u_id)==str(res[7]) and str(res[3])==date:
                    api.reply_msg(data,'error,already added ddl')
                    return

    else:
        id=sql.get_id_by_msg(remind_time_or_msg)
        if id:
            for i in range(len(id)):
                res=sql.get_ddl_by_id(id[i][0])
                if str(u_id)==str(res[7]) and str(res[3])==date:
                    api.reply_msg(data,'error,already added ddl')
                    return

    #print(111)
    if remind_time_or_msg.isdigit():
        sql.add_ddl(r_msg[3],str(r_msg[2])+':00',str(u_id),str(r_msg[1]),str(remind_time_or_msg))
        id=sql.get_ddl_id(r_msg[3],str(u_id),str(r_msg[1]))
        api.reply_msg(data,'success')
    else:
        sql.add_ddl(remind_time_or_msg,str(r_msg[2])+':00',str(u_id),str(r_msg[1]))
        id=sql.get_ddl_id(remind_time_or_msg,str(u_id),str(r_msg[1]))
        api.reply_msg(data,'success')

    cron_control.add(id,int(time[1]),real_day,real_h,real_min)


