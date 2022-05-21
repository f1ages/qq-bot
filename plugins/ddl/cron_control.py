from crontab import CronTab

def add(id,m,d,h,min='0'):
    cron=CronTab(user='root')
    com='python3 ~/qq/plugin/plugins/ddl/ddl_reminder.py -i '+str(id)
    job=cron.new(com,comment=str(id))
    job.month.on(m)
    job.day.on(d)
    job.hour.on(h)
    job.minute.on(min)
    cron.write()

def del_(id):
    cron=CronTab(user='root')
    edit_cron=CronTab(user='root')
    iter=cron.find_comment(str(id))
    for job in iter:
        edit_cron.remove(job)
    edit_cron.write()
