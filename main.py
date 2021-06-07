import admin
import student

#Function checks if the user is in the student database
def check_user(user,password):
    if user in admin.student_dict:
        if password == admin.student_dict[user].strip("\n"):
            name = user.replace("_"," ")
            print(f"Hello {name}")
            action=0
            while(action!=3):
                action = int(input("What would you like to do? \nView Info(1) \nChange Password(2) \nQuit(3)\n"))
                if(action==1):
                    student.desplay_info(user)
                elif(action==2):
                    name = user.replace('_',' ')
                    password = input("What would you like to change your password to?\n")
                    admin.change_student_password(name,password)
                elif(action==3):
                    print(f"Goodbye {name}")
                else:
                    print("Invalide input")
        else:
            print("Incorrect password")
    else:
        print("Student does not exist")

admin.update_dict()

#check if admin is using it with a input prompt
user = input("Enter username ")
key = input("Enter password ")
if user.lower()=='admin' and key=="Admin":
    print("Welcome Admin")
    action=0
    while action != 6:
        action = int(input("What would you like to do? \nAdd new Student(1) \nRemove student(2) \nUpdate grades(3) \nChange Student Password(4) \nView list of students(5) \nLogout(6)\n"))
        #python swichcase for action
        if action==1:
            name = input("Enter students name ")
            year = input("Enter students graduation year (yy) ")
            admin.add_student(name,year)
        elif action==2:
            name = input("Enter students name ")
            admin.remove_student(name)
        elif action==3:
            name = input("Enter students name ")
            admin.grade_student(name)
        elif action==4:
            name = input("Enter students name ")
            password = input("Enter new password ")
            admin.change_student_password(name,password)
        elif action==5:
            admin.list_students()
        elif action==6:
            print("Goodbye Admin")
        else:
            print("Invalid Input")
else:
    #check if user and password match a key-value in student dir
    check_user(user,key)

