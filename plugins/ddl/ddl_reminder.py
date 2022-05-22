import sys
sys.path.append('/root/qq/plugin')
import getopt
import api.api as api
import plugins.ddl.cron_control as cron_control
import api.sql as sql


def main(argv):

    user=''
    id=''

    try:
        opts,args=getopt.getopt(argv, "hu:i:",["user=","id="])
    except getopt.GetoptError:
        print('-u <user> -i <id>')
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print('-u <user> -i <id>')
            sys.exit()
        elif opt in ("-u","--user"):
            user=arg
        elif opt in ("-i","--id"):
            id=arg
    print(user)
    print(id)

    res=sql.get_ddl_by_id(id)
    print(res)
    msg='ddl remind: '+str(res[3])+' '+str(res[2])+'\t'+str(res[1])
    api.send_private_message(str(res[7]),msg)
    sql.update_remind_flag(id)
    cron_control.del_(id)
    sql.del_ddl_by_id(id)

if __name__ == '__main__':
    main(sys.argv[1:])

