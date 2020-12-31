#!/bin/bash

display_usage() {  
	echo -e "Usage: ./runc.sh <File.c>"
	} 

	if [  $# -ne 1 ] 
	then 
		display_usage
		exit 1
	else
        file_name=$1
        exe_file=${file_name%.c}
        gcc -o $exe_file $file_name
        ./$exe_file

	fi
