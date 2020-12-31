#!/usr/bin/python3

import requests
import gdown
import re
import os
import sys

def extract_files(url):
    ''' This Function to take URL and return dict of download link and file name'''
    folder_id = url[39:]
    files_id = {}

    res = requests.get(url)
    js = re.findall("<script>.*</script>", res.content.decode('utf-8'))
    title = re.findall("<title>(.*)</title>", res.content.decode('utf-8'))[0].split(" - ")[0]
    my_data = js[5].replace("null,", "").split("\\x22")
    
    for i in range(1, len(my_data)):
    	    if len(my_data[i]) == 33:
    		    	if my_data[i] not in folder_id:
                         files_id.update({my_data[i+4]:my_data[i]})

    return [files_id, title]

def download(files_id,title):
	''' This Function take a dict of file names and files id then download'''
	try:
		os.mkdir(title)
		for key,value in files_id.items():
			down_url = 'https://drive.google.com/uc?id='
			down_url += value
			output = os.getcwd() +'/'+ title+'/'+key
			gdown.download(down_url, output, quiet=False)
	except:
		for key,value in files_id.items():
			down_url = 'https://drive.google.com/uc?id='
			down_url += value
			output = os.getcwd() +'/'+ title+'/'+key
			if key not in os.listdir(os.getcwd()+'/'+title):
				gdown.download(down_url, output, quiet=False)
			else:
				print( key + " is Already Exist")


if __name__ == "__main__":
	try :
		url = sys.argv[1]
		download(extract_files(url)[0],extract_files(url)[1])
	except:
		print("Usage : python3 lazy_driver.py <Drive Url>")