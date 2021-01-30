#!/bin/bash

#given url must be in this form: https://www.facebook.com/SheikhMinshawi/videos/208459680399662
display_usage() {  
	echo -e "Usage: ./facebook-dl.sh <Url: https://www.facebook.com/USER/videos/ID>"
	} 
	if [  $# -ne 1 ] 
	then 
		display_usage
		exit 1
	else
		base_url="https://www.facebook.com/video.php?v="
		video_id=$(echo $1 | cut -d "/" -f 6)
		youtube-dl $base_url$video_id
	fi
