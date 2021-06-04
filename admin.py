import pathlib 
dict_path = pathlib.Path("student_dict.txt")
student_path = "students"
student_dict = {}

def update_dict():
    with dict_path.open('r') as file:
        lines = []
        student_dict.clear()
        #read from the file and put the pars into a dict as key - value 
        lines = file.readlines()
        for line in lines:
            user,password = line.split(',')
            student_dict[user] = password

def update_file():
    with dict_path.open('w') as file:
        for user,password in student_dict.items():
            file.write(f'{user},{password}\n')

def add_student(name,year):
    mod_name=name.replace(' ','_')
    with dict_path.open('a+') as file:
        if mod_name in student_dict:
            print("Student is alread in the system")
        else:
            file.write(f"{mod_name},{mod_name}_{year}\n")
            with open(f"{student_path}/{mod_name}.txt",'w+') as student_file:
                student_file.write(f"Name: {name} \nGraduation Year: 20{year} \nGPA: * \nCurrent Grades *|*|*|*|*|*|*|*")
    update_dict()

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
    update_dict()

def grade_student(name):
    mod_name=name.replace(' ','_')
    if mod_name not in student_dict:
            print("Student is not in the system")
    else:
        with open(f"{mod_name}.txt",'r+') as student_file:
            print(student_file.readlines)


def change_student_password(name,password):
    mod_name=name.replace(' ','_')
    if mod_name in student_dict:
        student_dict[mod_name]=password.strip("\n")
        update_file()
    else:
         print("Student is not in the system")

def list_students():
    for student in student_dict:
        name = student
        mod_name = name.replace('_',' ')
        print(mod_name)

