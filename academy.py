import sqlite3
'''Importing the module sqlit3'''
DB = sqlite3.connect("Academy.db")
CURSOR = DB.cursor()
CURSOR.execute('''CREATE TABLE IF NOT EXISTS staff (ID INT PRIMARY KEY,NAME TEXT,POSITION TEXT);''')
CURSOR.execute('''CREATE TABLE IF NOT EXISTS student (ID INT PRIMARY KEY,NAME TEXT,COURSE TEXT,PHASE INT);''')
def staff():
    '''Function to get the staff details form the user'''
    id_staff = int(input("Enter the ID:"))
    name_staff = input("Enter the staff name:")
    position_staff = input("Enter the position of the staff:")	
    CURSOR.execute('''INSERT INTO staff (ID,NAME,POSITION) VALUES(?,?,?);''', (id_staff, name_staff, position_staff))
def student():
    '''Function to get the student details from the student'''
    id_student = int(input("Enter student ID:"))
    name_student = input("Enter student name:")
    course_student = input("Enter student course:")
    phase_student = int(input("Enter phase:"))
    CURSOR.execute('''INSERT INTO STUDENT (ID,NAME,COURSE,PHASE) VALUES(?,?,?,?);''', (id_student, name_student, course_student, phase_student))
while True:
    print("ACADEMY")
    print("press 1 for staff\npress 2 for students\npress 3 for exit\n")  
    USER_INPUT = int(input("Enter your choice:"))
    if USER_INPUT == 1:
        REPEAT = 'yes'
        while(REPEAT == 'yes'):
            print("Staff Database")
            print("press 1 for new entry\npress 2 for viewing the data\n")
            NUM = int(input("Enter your choice:"))
            if NUM == 1:
                print("New entry\n")
                N = int(input("No of entry:"))
                for i in range(0, N):
                    staff(N)
                DB.commit()
                REPEAT = input("Enter yes if you want to continue:")
            if NUM == 2:
                print("Enter the details you want to view\n")
                POS = input("Enter the position:")
                CURSOR.execute('''SELECT ID,NAME,POSITION FROM staff WHERE position=?;''', (POS,))
                USER = CURSOR.fetchall()
                for row in USER:
                    print(row[0], row[1], row[2])
                REPEAT = input("Enter yes if you want to continue:")
        else:
            print("Exit")
    if USER_INPUT == 2:
        REPEAT = 'yes'
        while(REPEAT == 'yes'):
            print("Student details")
            print("press 1 for new entry\npress 2 for viewing deatils\n")
            NUM = int(input("Enter your choice:"))
            if NUM == 1:
                print("New entry\n")
                N = int(input("no of entry:"))
                for i in range(0, N):
                    student(N)
                DB.commit()
                REPEAT = input("Enter yes if you want to continue:")
            if NUM == 2:
                PHASE_TYPE = int(input("Enter the phase of the student:\n"))
                CURSOR.execute('''SELECT ID, NAME, COURSE, PHASE FROM student WHERE phase=?;''', (PHASE_TYPE,))
                for row in CURSOR:
                    print(row[0], row[1], row[2], row[3])
                NAME = input("Enter the student name:")
                CURSOR.execute('''SELECT ID, NAME, COURSE, PHASE FROM student WHERE name=?;''', (NAME,))
                USER = CURSOR.fetchone()
                print(USER)
                REPEAT = input("Enter yes if you want to continue:")
        else:
            print("exit")
    if USER_INPUT == 3:
        print("Exit")
        break
DB.commit()
DB.close()

