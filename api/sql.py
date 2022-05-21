import pymysql
import config

host=config.host
database=config.database
user=config.user
pwd=config.pwd
charset=config.charset

def a_check():

    return

'''modle controller'''

def using_m_check(admin=0):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    if admin == 1:
        sql='SELECT * FROM checker WHERE flag = 1'
    else:
        sql='SELECT * FROM checker WHERE flag = 1 and need_admin = 0'
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        db.close()
        return result
    except:
        return 'err'


def is_valiable_m_check(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='SELECT flag FROM checker WHERE id ='+str(id)
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()[0][0]
    except:
        return False

def get_m_id(name):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='SELECT id FROM checker WHERE name =\''+name+'\''
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()[0][0]
    except:
        return False

def valiable_m_check(admin):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    if admin == 1:
        sql='SELECT * FROM checker'
    else:
        sql='SELECT * FROM checker WHERE need_admin = 0'
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        db.close()
        return result
    except:
        return 'err'

def enable_m(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='UPDATE checker SET flag = 1 WHERE id = '+str(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()

def disable_m(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='UPDATE checker SET flag = 0 WHERE id = '+str(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()

def new_m(name,flag=0,need_admin=0,about=''):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='INSERT INTO checker (name,flag,need_admin,about) VALUE ('+name+','+str(flag)+','+str(need_admin)+','+about+')'
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()

def delete_m(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='DELETE FROM checker WHERE id = '+str(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        db.rollback()

'''ddl reminder'''

def add_ddl(msg,time,user_id,date,remind_time='60'):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='INSERT INTO ddl_remind (remind_msg,time,date,remind_time,user_id) VALUE (\''+msg+'\',\''+str(time)+'\',\''+str(date)+'\','+remind_time+',\''+user_id+'\')'
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()

def get_id_by_msg(msg):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='SELECT id FROM ddl_remind WHERE remind_msg = \''+str(msg)+'\''
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()
    except:
        return False

def get_ddl_id(msg,u_id,date):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='SELECT id FROM ddl_remind WHERE remind_msg = \''+str(msg)+'\' and user_id = '+str(u_id)+' and date = \''+date+'\''
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()[0][0]
    except:
        return False

def del_ddl():
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='DELETE FROM ddl_remind WHERE remind_flag = 1'
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        return False

def del_ddl_by_id(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='DELETE FROM ddl_remind WHERE id = '+str(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        return False

def update_flag(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='UPDATE ddl_remind SET flag = 1 WHERE id = '+str(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()

def update_remind_flag(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd)
    cursor=db.cursor()
    sql='UPDATE ddl_remind SET remind_flag = 1 WHERE id = '+str(id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()

def check_today_ddl(date):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd,charset=charset)
    cursor=db.cursor()
    sql='SELECT * FROM ddl_remind WHERE date = \''+str(date)+'\''
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()
    except:
        return False

def get_user_ddl(user_id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd,charset=charset)
    cursor=db.cursor()
    sql='SELECT * FROM ddl_remind WHERE user_id = '+str(user_id)
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()
    except:
        return False

def get_ddl_by_id(id):
    db=pymysql.connect(host=host,db=database,user=user,password=pwd,charset=charset)
    cursor=db.cursor()
    sql='SELECT * FROM ddl_remind WHERE id ='+str(id)
    try:
        cursor.execute(sql)
        db.close()
        return cursor.fetchall()[0]
    except:
        return False


