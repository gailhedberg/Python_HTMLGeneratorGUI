#!/usr/bin/end python
#
# gail hedberg - abc_db_utility.py using python 3.4
# august 4, 2015 - created
# 
# python drill #11

""" abc_db_utility.py  provides sqlite3 database access functions for the
abc_db.db
"""
from __future__ import unicode_literals
import sqlite3

#database location  - local
#db_name = 'C:\\Users\\Gail\\Documents\\TechAcademy\\abc_db.db'
db_name = 'abc_db.db'
text_list = [
        ("Summer Sale going on Now"),
        ("Get it while its cold - Big Winter Sale"),
        ("Back to school - stock up now!"),
        ("Under Constuction")
        ]


def exists(table_name='web_page_text'):
    # determine if the table exists
    try:
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute("Select * From {}".format(table_name))
        con.close()
        return True;
    except sqlite3.Error as e:
        return False;

def get_default_data():
    # create the table
    # load the table from the global var text_list
    # return
    global text_list

    try:
        con = sqlite3.connect(db_name)
        con.execute("DROP TABLE if EXISTS web_page_text")
        con.execute("CREATE TABLE web_page_text(body TEXT)")
        for i in text_list:
            #sql = "insert into web_page_text (body) values (?)", (i,)
            con.execute("insert into web_page_text (body) values (?)", (i,))
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print ("An error occurred - unable to load default data:\n\t {}".format(e.args[0]))

def get_table_data():
    # acccess the table
    # if successful, reload the global var text_list
    #    from the table rows
    # return
    global text_list
    temp_list = []

    try:
        con = sqlite3.connect(db_name)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM web_page_text")

        rows = cur.fetchall()
        for row in rows:
            temp_list.append(row[0])
        cur.close()

    except sqlite3.Error as e:
        print ("An error occurred - unable to get table data:\n\t {}".format(e.args[0]))

    if len(temp_list) > 0:
        text_list = temp_list

def get_web_text():
    
    global text_list
    if exists('web_page_text') == True:
        get_table_data()
    else:
        get_default_data()

    #print (text_list)
    return text_list

    
def update_web_text(text='web page under construction'):
    try:
        con = sqlite3.connect(db_name)
        con.execute("insert into web_page_text (body) values (?)",(text,))
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print ("A database update error occurred during update: {}".format(e.args[0]))
   
#get_web_text()

#update_web_text('time for a new sale')


        
