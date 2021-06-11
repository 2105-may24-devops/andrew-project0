#!/bin/bash
cd ~/ansible-project0
python3 -c 'import admin; admin.update_dict(); admin.remove_student("Test Student")'
cd ./students
if [ -f Test_Student.txt ]; then
	echo "Test failed"
	pwd
	exit 1
else
	echo "Test Successful"
fi
