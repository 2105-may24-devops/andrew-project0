#!/bin/bash

cd ..
python -c 'import admin; admin.add_student("Test Student", 93)'

if [ -f "~/ansible-project0/students/Test_Student.txt" ]; then
	echo "Test successful"
else
	echo "Test failed"
fi
