import pathlib
import time
import datetime
from types import new_class 
#path to the dictionary
dict_path = pathlib.Path("student_dict.txt")
#name of students folder
student_path = "students"
student_dict = {}
#time stamp for log file
t = time.time()
ts = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d_%H:%M:%S: ')

#update the dict to match all current info in the file
def update_dict():
    with dict_path.open('r') as file:
        lines = []
        student_dict.clear()
        #read from the file and put the pars into a dict as key - value 
        lines = file.readlines()
        for line in lines:
            user,password = line.split(',')
            student_dict[user] = password

#update the file to match the current dict
def update_file():
    with dict_path.open('w') as file:
        for user,password in student_dict.items():
            file.write(f'{user},{password}\n')

#adds a new student to the file then calls update dict
def add_student(name,year):
    mod_name=name.replace(' ','_')
    with dict_path.open('a+') as file:
        if mod_name in student_dict:
            print("Student is already in the system")
        else:
            file.write(f"{mod_name},{mod_name}_{year}\n")
            with open(f"{student_path}/{mod_name}.txt",'w+') as student_file:
                student_file.write(f"Name: {name} \nGraduation Year: 20{year} \nCurrent Grades *|*|*|*|*|*|*|*")
            with open("log.txt",'a') as log:
                log.write(f"{ts}Admin added {name} as a new student.\n")
    update_dict()

#rewrites the file without the student then calls update dict
def remove_student(name):
    mod_name=name.replace(' ','_')
    if mod_name not in student_dict:
            print("Student is not in the system")
    else:
        with dict_path.open('r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                current_name = line.split(",")
                if mod_name != current_name[0]:
                    file.write(line)
        student_file = pathlib.Path(f"{student_path}/{mod_name}.txt")
        student_file.unlink()
        with open("log.txt",'a') as log:
            log.write(f"{ts}Admin removed {name} from the list of students.\n")
    update_dict()

#ment to change * in student file to a set of grades
def grade_student(name):
    mod_name=name.replace(' ','_')
    if mod_name not in student_dict:
            print("Student is not in the system")
    else:
        with open(f"{student_path}/{mod_name}.txt",'r') as student_file:
            lines = student_file.readlines()

            for line in lines:
                pass
            mod_line = list(line)
            for i in range (1,16,2):
                grade = str(input("Grades from 8th to 1st "))
                mod_line[len(line)-i] = grade
            line = "".join(mod_line)
        with open(f"{student_path}/{mod_name}.txt",'w') as student_file:
            for new_line in lines:
                if "Current" not in new_line:
                    student_file.write(new_line)
                else:
                    student_file.write(line)
        with open("log.txt",'a') as log:
            log.write(f"{ts}Admin changed {name}'s grades.\n")
            
                    

#change the password in the dict then calls update file
def change_student_password(name,password):
    mod_name=name.replace(' ','_')
    if mod_name in student_dict:
        student_dict[mod_name]=password.strip("\n")
        update_file()
        with open("log.txt",'a') as log:
            log.write(f"{ts}{name}'s password was changed.\n")
    else:
         print("Student is not in the system")

#print current dict
def list_students():
    for student in student_dict:
        name = student
        mod_name = name.replace('_',' ')
        print(mod_name)
