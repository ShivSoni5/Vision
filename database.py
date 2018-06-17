#!/usr/bin/python3

import mysql.connector as mysql
from time import asctime


def log(query):
    time=asctime()
    mariadb = mysql.connect(user='username',password='password',database='Vision') #change username and password
    cursor = mariadb.cursor()
    query = (f'insert into logs(logs,Time) values("{query}","{time}");')
    cursor.execute(query)
    mariadb.commit()
    mariadb.close()

def get_log():
    mariadb = mysql.connect(user='username',password='password',database='Vision') #change username and password
    cursor = mariadb.cursor()
    cursor.execute('select count(*) from logs;')
    n = cursor.fetchall()
    cursor.execute(f'select logs from logs limit 10 offset {n[0][0]-10};')
    logs = cursor.fetchall()
    return logs
#    for i,log in enumerate(logs):
#        print(f'{i+1}. {log[0]}')

if __name__=='__main__':
    get_log()
    
