#import sqlite3

#conn = sqlite3.connect("books.sqlite")

#cursor = conn.cursor()
#sql_query = """ CREATE TABLE book (
 #   id integer PRIMARY KEY,
  #  author text NOT NULL,
   # language text NOT NULL,
    #title text NOT NULL
#)"""
#cursor.execute(sql_query)

import pymysql

conn = pymysql.connect(
    host='sql6.freesqldatabase.com',
    database='sql6474081',
    user='sql6474081',
    password='rlivYyUN5E',
    charset='utf8mb4',
    # cursorclass=pymysql.cursors.DictCursor
    cursorclass=pymysql.cursors.DictCursor
)
 
cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()