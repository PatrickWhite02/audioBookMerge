import os
import subprocess
try:
        import eyed3
except:
        print("User has not installed eyed3, will not tag audio")
		
k1=os.getcwd()
#for each folder in Audio
for i2 in os.listdir():
	#reset working directory to root folder
	os.chdir(k1)
	if(os.path.isdir(os.path.join(os.getcwd(), i2))):
		k2=os.path.join(os.getcwd(), i2)
		#change dir to Book
		os.chdir(k2)
		print(k2)
		#for each folder in Book
		for i3 in os.listdir():
			os.chdir(k2)
			if(os.path.isdir(os.path.join(os.getcwd(), i3))):
				k3=os.path.join(os.getcwd(), i3)
				#change folder to DISC 1
				os.chdir(k3)
				locationForCombined=str(k2 + "\\" + i3 + ".mp3")
				command="copy /b *.mp3 \"" + locationForCombined +"\""
				#will generate a file at the bottom of each disc folder called i3 with each mp3 file from that disc merged together
				subprocess.call(command, stdin=None, stdout=None, stderr=None, shell=True)
	#once we've made the compilations for each disc but before we move on to the next book merge them into groups of 5
	os.chdir(k2)
	numDisk=0#number of disks
	#determine how many groups to make
	comps=[]
	for j in os.listdir():
		if(".mp3" in j):
			numDisk=numDisk+1
			comps.append(j)
	if(numDisk%5==0):
		numGroups=int(numDisk/5)
	else:
		numGroups=int(numDisk/5) + 1#number of groups to put the disks in
	#put them into order, I can't rely on system order because of 1, 10, 11, 2
	orderedComps=[]
	for l in comps:
		if(len(l)<11):
			orderedComps.append(l)
	for x in comps:
		if(not len(x)<11):
			orderedComps.append(x)
	#put them into their groups
	for y in range (0, numGroups):
		if not y == numGroups-1:
			ran=((y+1)*5)
			#part of command string that contains each file
			auds=""
			#1..5 6...10 etc...
			for z in range ((y*5)+1, ran):
				auds=auds + " \"Disc " + str(z) + ".mp3\" +"
			auds=auds + " \"Disc " + str(z+1) + ".mp3\""				
			command="copy /b" + auds + " " + str((y*5)+1) + "-" + str(ran) + ".mp3"
			subprocess.call(command, stdin=None, stdout=None, stderr=None, shell=True)
			try:
                                #tag the generated
				audiofile=eyed3.load(str((y*5)+1) + "-" + str(ran) + ".mp3")
				audiofile.tag.artist = "Audiobooks"
				audiofile.tag.album = i2
				audiofile.tag.title = str((y*5)+1) + "-" + str(ran)
				audiofile.tag.track_num = y+1
				audiofile.tag.save()
			except:
				print("knobs")
		else:
			auds=""
			ran=numDisk
			q=0
			for q in range ((y*5)+1, numDisk):
				auds=auds + " \"Disc " + str(q) + ".mp3\" +"
			auds=auds + " \"Disc " + str(q+1) + ".mp3\""				
			command="copy /b" + auds + " " + str((y*5)+1) + "-" + str(ran) + ".mp3"
			subprocess.call(command, stdin=None, stdout=None, stderr=None, shell=True)
			try:
				#tag the generated
				audiofile = eyed3.load(str((y*5)+1) + "-" + str(ran) + ".mp3")
				audiofile.tag.artist = "Audiobooks"
				audiofile.tag.album = i2
				audiofile.tag.title = str((y*5)+1) + "-" + str(ran)
				audiofile.tag.track_num = y+1
				audiofile.tag.save()
			except:
				print("knobs")