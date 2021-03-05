from flask import Flask
from flask_mysqldb import MySQL

class Database:
    server = 'localhost'
    user = 'root'
    password = 'Supadupa1234?'
    dbname = 'flask_bonsai'
    mysql= MySQL()    
    def __init__(self,server,user,password,dbname,app):
        self.server = server
        app.config['MYSQL_HOST'] = server
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = password
        app.config['MYSQL_DB'] = dbname
        print('Configured db')
        
        
