#!/bin/bash

cd ~/ansible-project0/
python3 -c 'import admin; admin.add_student("Test Student", 93)'

cd ./students
if [ -f Test_Student.txt ]; then
	echo "Test successful"
else
	echo "Test failed"
	pwd
	exit 1
fi
