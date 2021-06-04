def desplay_info(student_username):
    with open(f'{student_username}.txt','r') as file:
        for line in file.readlines():
            print(line)
