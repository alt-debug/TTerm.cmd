import os, time, platform, shutil, socket, getpass, multiprocessing, sys
import webbrowser as web # Webbrowser for openLink command
import subprocess as sp # Subprocess for ping
import datetime as dt # Datetime for date and time
from time import gmtime, strftime

username = getpass.getuser()

hostname = socket.gethostname()











__cache__ = 0 # Set cache to 0
prompt = '' # Setup prompt variable
__os__ = platform.system() # Get operating system name and store it in a variable (const)

# Print version and title as function
def title():
    print('@------------------------------------------------------------------------------------@')
    print('|                                                                                    |')
    print('|                                  |PyTerm v0.5.0|                                   |')
    print('|                                                                                    |')
    print('@------------------------------------------------------------------------------------@')

changelog_message = 'First Release of TTerm!'

def clear(): # Clear screen
    if __os__ == 'Windows': # Windows
        os.system('cls')
    else: # Linux and Mac OS X
        os.system('clear')

def flt(param): # Return float from param
    return float(param)

def ping(host): # Ping a server
    param = '-n' if platform.system().lower() == 'windows' else '-c' # Setup ping parameters
    command = ['ping', param, '4', host]  # 
    return sp.call(command) == 0

def fileExists(fileName):
	return os.path.exists(fileName)

def setupColor():
    try:
        f = open('user_data/settings/color.txt', 'r')
        os.system(f.read())
    except:
        os.system('color 0A')


def cache():
    try:
        if fileExists('user_data'):
            if fileExists('user_data/cache.txt'):
                cache = open('user_data/cache.txt', 'r')
                if '1' in cache.read():
                    __cache__ = 1
                else:
                    cache_ = open('user_data/cache.txt', 'w')
                    cache_.write('1')
                    __cache__ = 0
            else:
                cache = open('user_data/cache.txt', 'x')
                cache.write('1')
                __cache__ = 0
        else:
            os.mkdir('user_data')
            cache = open('user_data/cache.txt', 'x')
            cache.write('1')
            __cache__ = 0
    except:
        print('Error')
    
def promptUpdate(): # Update prompt
    if fileExists('user_data/settings'):
        if fileExists('user_data/settings/prompt.txt'):
            global prompt
            prompt = open('user_data/settings/prompt.txt', 'r').read()
        else:
            f = open('user_data/settings/prompt.txt', 'x')
            f.write('>')
            f.close()
            prompt = '>'
    else:
        os.mkdir('user_data/settings')
        f = open('user_data/settings/prompt.txt', 'x')
        f.write('>')
        f.close()
        prompt = '>'

def fopenLink(link):
    web.open(link)




while True:
    print(prompt+' ', end='') # Input prompt without line break ( \n )
    cmd = input('') # Collect input
    if cmd == 'help':
        print('changelog                               Shows TTerms Changelog')
        print('help_advanced                           Shows a more advanced help menu')
        print('more coming soon! like findDir, the ls command, and cd command!')
        print("time                                    Shows your time")
        print('date                                    Shows your datetime')
    elif cmd == 'help_advanced':
        print('ping [HOSTNAME]                                   Pings the hostname you chose')
        print('hostname                                 Shows your device hostname')
        print('ipaddress                                Shows your CORRECT device ip')
        print('more advanced commands coming soon!')
    elif cmd == 'changelog':
        print(changelog_message)
    elif cmd == 'time':
        print('add this when you get to gammys house')
    elif cmd == 'date':
        print('add this when you get to gammys house')
    elif cmd == 'hostname':
        print(hostname)
