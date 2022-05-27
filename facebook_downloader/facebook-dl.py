#!/usr/bin/env python3

from sys import argv
from re import findall
import subprocess
from termcolor import colored

REGEX='^(https?://www.facebook.com/watch\?v=\d{15})$'

def download(id):
    base_url="https://www.facebook.com/video.php?v="
    cmd = subprocess.Popen(["youtube-dl",base_url+id], stderr=subprocess.STDOUT)
    stdout,stderr = cmd.communicate()
    if stderr == None:
        print (colored('[+] Video Has Been Downloaded Successfully!', 'green'))
    else:
        print(stderr)

if __name__ == "__main__":
    try:
        url = argv[1]
        state = findall(REGEX, url)
        
        if state:
            vid = url.split("=")[1]
            download(vid)
        else:
            vid = url.split("/")[-1]
            download(vid)
    except:
        print("Usage: facebook-dl.py URL")