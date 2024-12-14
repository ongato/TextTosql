
import sqlite3
Connection=sqlite3.connect("store.db")
cursor=Connection.cursor()
table_info="""
create table STORE(NAME VARCHAR(25),ITEM_CODE INT,QUANTITY INT,STOCK INT);
"""
cursor.execute(table_info)
cursor.execute(''' Insert into STORE values ('TV-1234', 1001, 50, 200)''')
cursor.execute(''' Insert into STORE values ('Washing Machine', 1002, 10, 50)''')
cursor.execute(''' Insert into STORE values ('Air Conditioner', 1004, 30, 120)''')
cursor.execute(''' Insert into STORE values ('Smartphone', 1005, 40, 150)''')
cursor.execute(''' Insert into STORE values ('Microwave', 1006, 20, 80)''')

print("the inserted records are ")
data=cursor.execute('''select * from store ''')
for row in data :
    print(row)

Connection.commit()
Connection.close()