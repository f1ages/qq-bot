import config
import api.sql as sql
import plugins.price as price
import plugins.help as help
import plugins.xcx as xcx
import plugins.set_moudle_flag as set_moudle_flag
import plugins.ddl.ddl_adder as ddl_adder
import plugins.ddl.my_ddl as my_ddl
import plugins.ddl.ddl_help as ddl_help

def main(data):
    if(data['post_type']=='message'):

        if str(data['sender']['user_id'])==config.master_id:#master

            if str(data['message_type'])=='group':#群组
                if str(data['message'])[0]=='!':
                    set_moudle_flag.main(data)

                elif str(data['message'])[0]=='%':
                    if price_check() == 1:
                        price.main(data)

                elif str(data['message'])=='?plugin':
                    help.main(data)

                elif str(data['message'])=='?active':
                    help.usage(data)

                elif str(data['message'][:8])=='add ddl;' or str(data['message'][:8])=='add ddl；':
                    if ddl_check()==1:
                        ddl_adder.main(data)

                elif str(data['message'][:10])=='check ddl?' or str(data['message'][:10])=='check ddl？':
                    if ddl_check()==1:
                        my_ddl.main(data)

                elif str(data['message'][:8])=='del ddl:' or str(data['message'][:8])=='del ddl：':
                    if ddl_check()==1:
                        my_ddl.del_ddl(data)

                elif str(data['message'])=='?ddl help' or str(data['message'])=='？ddl help':
                    if ddl_check()==1:
                        ddl_help.main(data)


                return

            elif str(data['message_type'])=='private':#私聊

                if str(data['message'])[0]=='!':
                    set_moudle_flag.main(data)

                elif str(data['message'])[0]=='%':
                    if price_check()==1:
                        price.main(data)

                elif str(data['message'])=='?plugin':
                    help.main(data,1)

                elif str(data['message'])=='?active':
                    help.usage(data,1)

                elif str(data['message'][:8])=='add ddl;' or str(data['message'][:8])=='add ddl；':
                    if ddl_check()==1:
                        ddl_adder.main(data)

                elif str(data['message'][:10])=='check ddl?' or str(data['message'][:10])=='check ddl？':
                    if ddl_check()==1:
                        my_ddl.main(data)

                elif str(data['message'][:8])=='del ddl:' or str(data['message'][:8])=='del ddl：':
                    if ddl_check()==1:
                        my_ddl.del_ddl(data)

                elif str(data['message'])=='?ddl help' or str(data['message'])=='？ddl help':
                    if ddl_check()==1:
                        ddl_help.main(data)

                return
        else:                                       #公开

            if str(data['message_type'])=='group':#群组

                if str(data['message'])[0]=='%':
                    if price_check()==1:
                        price.main(data)

                elif str(data['message'])=='?active':
                    help.usage(data)

                elif str(data['message'][:8])=='add ddl;' or str(data['message'][:8])=='add ddl；':
                    if ddl_check()==1:
                        ddl_adder.main(data)

                elif str(data['message'][:10])=='check ddl?' or str(data['message'][:10])=='check ddl？':
                    if ddl_check()==1:
                        my_ddl.main(data)

                elif str(data['message'][:8])=='del ddl:' or str(data['message'][:8])=='del ddl：':
                    if ddl_check()==1:
                        my_ddl.del_ddl(data)

                elif str(data['message'])=='?ddl help' or str(data['message'])=='？ddl help':
                    if ddl_check()==1:
                        ddl_help.main(data)

                if xcx_check()=='1':
                    xcx.main()
                return

            elif str(data['message_type'])=='private':#私聊

                if str(data['message'][:8])=='add ddl;' or str(data['message'][:8])=='add ddl；':
                    if ddl_check()==1:
                        ddl_adder.main(data)

                elif str(data['message'][:10])=='check ddl?' or str(data['message'][:10])=='check ddl？':
                    if ddl_check()==1:
                        my_ddl.main(data)

                elif str(data['message'][:8])=='del ddl:' or str(data['message'][:8])=='del ddl：':
                    if ddl_check()==1:
                        my_ddl.del_ddl(data)

                elif str(data['message'])=='?ddl help' or str(data['message'])=='？ddl help':
                    if ddl_check()==1:
                        ddl_help.main(data)

                return

def price_check():
    id=sql.get_m_id('price')
    return sql.is_valiable_m_check(id)

def xcx_check():
    id=sql.get_m_id('xcx')
    return sql.is_valiable_m_check(id)

def ddl_check():
    id=sql.get_m_id('ddl_reminder')
    return sql.is_valiable_m_check(id)