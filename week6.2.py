import sqlite3

conn = sqlite3.connect(r'D:\Watcharachat_Python\watcharachat.db')
c = conn.cursor()
# Create table
'''
c.execute("""CREATE TABLE students (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    age varchar(5) NOT NULL,
    sex varchar(10) NOT NULL,
    email varchar(10) NOT NULL,
    tel varchar(10) NOT NULL
    Runningtype(30))""")
conn.commit()
conn.close()
'''

def menu():
    global choice
    print('-'*7,'ระบบลงทะเบียนผู้สมัครวิ่งมาราธอน','-'*7)
    print('='*30,'\nเพิ่มข้อมูลผู้สมัคร กด [a]\nแสดงข้อมูลผู้สมัคร [s]\nแก้ไขข้อมูลผู้สมัคร [e]\nลบข้อมูลผู้สมัคร [d]\nออกจากระบบ [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')

def add(fname,lname,id,age,sex,email,tel,Runningtype):
    try :
        conn = sqlite3.connect(r'D:\Watcharachat_Python\watcharachat.db')
        c = conn.cursor()
        sql = '''INSERT INTO students (fname,lname,id,age,sex,email,tel,Runningtype) VALUES (?,?,?,?,?,?,?,?)'''
        data = (fname,lname,id,age,sex,email,tel,Runningtype)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('ได้เพิ่มข้อมูลเรียบร้อย')

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

def show():
    conn = sqlite3.connect(r'D:\Watcharachat_Python\watcharachat.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM students''')
    result = c.fetchall()
    print('{0:<12}{1:<15}{2:<15}{3:<27}{4:<6}{5:<6}{6}'.format('ลำดับที่',' ชื่อ','สกุล','อายุ','เพศ','อีเมล','เบอร์โทรศัพท์','ประเภทการวิ่ง'))
    for x in result :
        print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<6}{5:<6}{6}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
    print('ได้ทำรายการเสร็จสิ้น\n')
    conn.commit()
    conn.close()

def edit(fname,lname,email,sex,age,year,iid):
    conn = sqlite3.connect(r'D:\Watcharachat_Python\watcharachat.db')
    c = conn.cursor()
    try :
        data = (fname,lname,email,sex,age,year,'{}'.format(iid))
        c.execute('''UPDATE students SET fname =?, lname =?, email =?, sex =?, age =?, year =? WHERE id = ?''',data)
        conn.commit()
        c.close()
        print('ได้แก้ไขข้อมูลเรียบร้อยแล้ว\n')
        
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

def delete(del_id):
    conn = sqlite3.connect(r'D:\Watcharachat_Python\watcharachat.db')
    c = conn.cursor()
    try :
        c.execute('DELETE FROM students WHERE id = {}'.format(del_id))
        conn.commit()
        c.close()
        print('ได้ลบข้อมูลเรียบร้อย\n')       

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

while True:
    menu()       
    if choice == 'a':
        fn,ln,em,s,a,y = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        add(fn,ln,em,s,a,y)
    elif choice == 's':
        show()
    elif choice == 'e':
        iid = input('เลือกลำดับที่ต้องการแก้ไข : ')
        efn,eln,eem,es,ea,ey = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        edit(efn,eln,eem,es,ea,ey,iid)
    elif choice == 'd':
        del_id = input('เลือกลำดับที่ต้องการลบ : ')
        delete(del_id)

    elif choice == 'x':
        yesno = input('ต้องการออกจากระบบหรือไม่ [y/n]: ')
        if yesno == 'Y' or yesno == 'y':
            print('ได้ออกจากระบบแล้ว')
            break
        elif yesno == 'N' or yesno == 'n':
            print('ได้ทำการกลับสู่ระบบแล้ว')
            continue