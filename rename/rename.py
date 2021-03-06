import os
from mp3_tagger import MP3File
import threading 

def change_name(dir):
	for file in files:

		if file.endswith(".mp3"):
			
			mp3 = MP3File(file)
			tags = mp3.get_tags()
			ac_name = tags["ID3TagV1"]["song"]
			new_name = file.replace(".mp3", "") +"-"+ ac_name

			if ac_name in file:
				print(file + " is already Renamed")
			else:
				os.rename("./" + file , "./" + new_name + ".mp3")
				print("[+] File Name Changed From " + file + " to " + new_name + ".mp3")
		else:
			pass

if __name__ == "__main__":
		
	files = os.listdir(".")
	t1 = threading.Thread(target=change_name, args=(files,))
	t1.start()
	t1.join()
	print("All File Names Changed Successfully")
