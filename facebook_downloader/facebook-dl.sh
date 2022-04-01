#!/bin/bash

#given url must be in this form: https://www.facebook.com/SheikhMinshawi/videos/208459680399662
# https://www.facebook.com/watch?v=434130678324366
display_usage() {  
	echo -e "Usage: ./facebook-dl.sh URL Form"
	echo -e "Form = 0 : https://www.facebook.com/USER/videos/ID"
	echo -e "Form = 1 : https://www.facebook.com/watch/?v=ID"
	} 
	if [  $# -ne 2 ] 
	then 
		display_usage
		exit 1
	else
		base_url="https://www.facebook.com/video.php?v="
		if [ $2 = 0 ]
		then
			video_id=$(echo $1 | cut -d "/" -f 6)
			youtube-dl $base_url$video_id
		elif [ $2 = 1 ]
		then
			video_id=$(echo ${1:(-15)})
			youtube-dl $base_url$video_id
		else
			echo "Invalid Form!"
			display_usage
			exit 1
		fi
	fi
