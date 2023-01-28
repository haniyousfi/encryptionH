def runfiles():
	import os
	import sys 
	#show path
	import subprocess
	subprocess.run(["cd"], capture_output = True).stdout.decode()
	pwd= subprocess.run(["pwd"], capture_output = True).stdout.decode()
	path= subprocess.run(["ls","-R"], capture_output = True).stdout.decode()
	with open("allfiles.txt","w") as allfiles:
		allfiles.write(path)
	with open("allfiles.txt","r") as allfiles:
        	listefiles=[]
        	listefiles=allfiles.readlines()
	listefilesplus=[]
	for i in listefiles:
        	if (len(i)>3):
        		if (i[-2]==":"):
        			A=i[1:-2]
        			A=pwd[0:-1]+A
        			listefilesplus.append(A)
	return listefilesplus
h=[]
h=runfiles()
print(h)
