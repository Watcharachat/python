import sqlite3 #import sqlite3

def inserttousers (fnme,IName,email):
    try :
       # conn = sqlite3.connect("D:\Watcharachat_Python\example.db")
       # c = conn.cursor() #create a cursor object 
       # sql = ''' INSERT INTO users (fnme,IName,email) VALUES (?,?,?)'''
        data = ('B','B','B'),('C','C,C'),('D','D','D')
        c.executemany('INSERT INTO users (fnme,IName,email.) VALUES (?,?,?)',data) 
        conn.commit() 
        c.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close()

#inserttousers('Guido','Rossum','Python@gmail.com')
#inserttousers('Dennis','Ritchie','abc')