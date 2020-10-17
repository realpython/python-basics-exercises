import mysql.connector
import pyautogui

mypasswd=pyautogui.prompt('Enter your mysql password')
mydb=mysql.connector.connect(host='localhost', user='root', password=mypasswd)
cur=mydb.cursor()
cur.execute('create database if not exists rdm123')

mydb1=mysql.connector.connect(host='localhost',
                            user='root',
                            password=mypasswd,
                            database='rdm123')
cur1=mydb1.cursor()
cur1.execute('create table if not exists abc(number int(2) primary key not null auto_increment, name varchar(20), gender varchar(1))')

name=pyautogui.prompt('Enter Name')
gender=pyautogui.prompt('Enter Gender')

print(name)

if name!=None or gender!=None:
    data1=(name,gender)
    cur1.execute('insert into abc(name , gender) values (%s,%s)',data1)
    mydb1.commit()
    pyautogui.alert('Data Filled Successfully.')
else:
    pyautogui.alert('Data Filling Cancelled')

show=pyautogui.confirm(text='Would you like to show the databases?', buttons=['Yes','No'])

if show == 'Yes':
    cur1.execute('select * from abc')
    shwd=cur1.fetchall()
    pyautogui.alert(shwd)
    print('SUCCED!')
else:
    print('NOT SUCCED!')