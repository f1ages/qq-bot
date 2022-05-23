import api.api as api
help_text = '''Powered by F1ag, bug report: https://github.com/f1ages/qq-bot/issues
功能:
\t创建个人ddl列表，增加或删除ddl事项，可随时查看列表，并在设定时间私戳提醒，提醒后自动删除，再也没有错过ddl的烦恼！！！
命令：
\t① check ddl?\t查看当前ddl列表
\t② del ddl:{real id}\t删除ddl事项
\t\t\treal id:查询列表返回的id号
\t③ add ddl%3B{date}%3B{time}%3B{remind_msg}%3B[remind_time]\t添加ddl事项
\t\t\tdate:日期 格式如：2022-5-22
\t\t\ttime:时间 格式如：20:00
\t\t\tremind_msg:ddl事项名
\t\t\tremind_time(可选):提前于设定时间多少分钟提醒
'''

def main(data):
    #print(help_text)
    api.reply_msg(data, str(help_text))

