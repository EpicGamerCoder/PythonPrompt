import os
import sys
import time
import random
import argparse
import webbrowser
import subprocess
import platform
import modules.help
import modules.volume_name
import modules.slashquestion.queue
from modules.wte import wte
from pathlib import Path
from configparser import ConfigParser
from modules.logsetup import ilog
from os import environ

# Setting crutial varibles
inum = random.randint(0, 1000000)
ilog("Instace Number: " + str(inum))

# Know what version of PythonPrompt you are running.
# This can be edited using the -v flag.
appversion = "Pre-Alpha 1.0.1"
# What edit version this file is. 001 means 1st Release and so on.
build = "002"
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--version", action='store', help='Set the Current Version manually')
parser.add_argument("-lv", "--lversion", action='store', help='Set the Latest Version manually')
parser.add_argument("--title", action='store', help='Set the Window Title')
parser.add_argument("--emandroid", action="store_true", help='Force set the OS to Andoird')
parser.add_argument("--emwindows", action="store_true", help='Force set the OS to Windows')
parser.add_argument("--emlinux", action="store_true", help='Force set the OS to Linux')
parser.add_argument("-f", "--forced", action="store_true", help='Disable checking for updates or any checks in general')
parser.add_argument("--appath", action="store", help="Set the appath (EXPERIMENTAL - WILL CAUSE ERRORS IF NOT SETUP)")

args=parser.parse_args()
if args.forced:
    forced = True
    ilog("<<< Running in forced mode >>>")
else:
	forced = False

if not args.version == None:
	appversion = args.version
	cav = True
	ilog("Using custom appversion: " + str(appversion))
else:
	cav = False

if not args.lversion == None:
	lappversion = args.lversion
	lcav = True
	ilog("Using custom lappversion: " + str(lappversion))
else:
	lcav = False

if not args.appath == None:
	cap = True
	fcap = False
	if os.path.isdir(args.appath):
		appath = args.appath
		appath = appath + "/"
		ilog("Using coustom appath: " + args.appath)
	else:
		if not forced:
			print("The folder does not exist, cannot use as an appath.")
			input("Press anything to exit.")
			quit()
		else:
			cap = True
			fcap = True
			appath = args.appath
			appath = appath + "/"
			ilog("Using coustom appath: " + args.appath)
			ilog("The coustom appath does not exist but forced mode is enabled, so the varible is being used.")
else:
	cap = False
	fcap = False
	
if args.emandroid:
	OS = "Andoird"
if args.emwindows:
	OS = "Windows"
if args.emlinux:
	OS = "Linux"

config = ConfigParser()
if not 'appath' in locals():
	appath = os.getcwd().replace('\\','/')
	appath = appath + "/"
ilog("appath: " + appath)
set1 = time.perf_counter()
ilog("Setup timer started!")
ilog("Preparing debug log...")
setd1 = time.perf_counter()
open('modules/config/logs/debug.log', 'w').close()

def print_to_file(filename):
    orig_stdout = sys.stdout    
    
    class Unbuffered:
        def __init__(self, filename):
            self.stream = orig_stdout
            self.te = open(filename,'w')        
            
        def write(self, data):
            self.stream.write(data)
            self.stream.flush()
            self.te.write(data)
            self.te.flush()
        
        def flush(self):
        	pass    
        	
    sys.stdout=Unbuffered(filename)
 
print_to_file('modules/config/logs/debug.log')
setd2 = time.perf_counter()
ilog("Debug Log prepared and activated!")
ilog("Checking Operating System...")
setos1 = time.perf_counter()

if 'OS' not in globals():
    if 'ANDROID_BOOTLOGO' in environ:
        OS = "Android"
        print("Android OS - usage not reccomended (yet).")
        print("Type C to continue (for testing/development purposes)")
        print("Type anything else to exit")
        cho = input(">>>")
        if ((cho == "C") or (cho == "c")):
            pass
        else:
            quit()
    else:
        OS = str(platform.system())
        if OS == "Windows":
        	import ctypes
        	ctypes.windll.kernel32.SetConsoleTitleW("PythonPrompt")
        elif OS == "Linux":
        	print('\33]0;PythonPrompt\a', end='', flush=True)
        elif OS == "Darwin":
	        OS = "MacOS"
	        sys.stdout.write("\x1b]2;PythonPrompt\x07")
        else:
	        print("Operating System not supported (" + OS + ").")
	        print("To force launch PythonPrompt, use the flag '--emandoird' or '--emwindows' or '--emlinux'")
	        input("Press anything to exit")
	        quit()
        	
setos2 = time.perf_counter()
ilog("Operating System detected: " + OS)
ilog("Redefining function names and setting varibles...")
setfv1 = time.perf_counter()
help = modules.help.help
helpi = modules.help.helpi
helpdev = modules.help.helpdev
helpdebug = modules.help.helpdebug
volume_name = modules.volume_name.volname
slashqueue = modules.slashquestion.queue.slashqueue
if not "lappversion" in locals():
	lappversion = ""
if not "appversion" in locals():
	appversion = ""

# Setting the User Varibles dictionary
uservar = {}
uservar["appath"] = appath
uservar["os"] = OS
uservar["args"] = args

# Reading config.ini
#bool_val = config.getboolean('section_a', 'bool_val')
#float_val = config.getfloat('section_a', 'pi_val')
if not os.path.isfile(appath + 'modules/config/config.ini'):
	print("Config file does not exist.")
	print("Using default values...")
	ilog("config.ini does not exist.")
	syscommand = "Disabled"
	message = "Disabled"
	extracommands = False
	timeout = 0
else:
	config.read(appath + 'modules/config/config.ini')
	syscommand = config.get('main', 'syscommands')
	message = config.get('main', 'message')
	extracommands = config.getboolean('main', 'extracommands')
	timeout = config.getint('main', 'timeout')
ilog("syscommands: " + syscommand)
ilog("extracommands: " + str(extracommands))
if extracommands:
	from modules.config.exc import excommand
ilog("Redefinition and varible creation complete!")
ilog("Creating cmd functions...")

def cls():
	os.system('cls||clear')
	return

def lcls():
	os.system('cls||clear')
	print("This app is in Pre-Alpha and not ready for use yet.")
	print("Only some commands work as of now.")
	print("\nFor the command 'echo', varibles do not work. (To check varible contents use the command 'echovar')")
	print("For a list of commands that are supported, use the command 'help'")
	if message != "Disabled":
		print(message)
	return
	
def echo(text):
	if "%" in text:
		text = text.replace('%', 'uservar[', 1)
		text = text.replace('%', ']', 1)
		text = text.replace("'", "", 1)
		text = text.replace("'", "", 1)
	print(text)
	return
	
def set(varn, varc):
	uservar[varn] = varc
	print("Set " + varn + " as " + uservar[varn])
	
def echovar(text):
	text = text.translate({ord(c): None for c in "%"})
	if text in uservar:
		print(uservar[text])
		return
	print("Varible does not exist!")
	return
	
def cd(folder):
	if folder == "\\":
		folder = volume_name(os.getcwd())
	else:
		folder = folder[1:]
	if not os.path.isdir(folder):
		print("Directory does not exist.")
		return
	os.chdir(folder)
	
def delcmd(fdir):
    fdir = Path(fdir)
    if fdir.exists():
        if fdir.is_file():
            os.remove(fdir)
            print("The file was removed")
        if fdir.is_dir():
             os.rmdir(fdir)
             print("The folder was deleted (along with the contents inside)")
    else:
        print("The file / folder does not exist!")
        
def mkdir(foldername):
	path = os.path.join(os.getcwd(), foldername)
	os.mkdir(path)
	
def mkfile(filename):
	path = os.path.join(os.getcwd(), filename)
	with open(path, 'w'): 
	    pass

def version(startup = False, force = False):
	global lappversion
	global appversion
	if not startup and not force:
		print("Latest PythonPrompt Version: " + lappversion)
		print("Current PythonPrompt Version: " + appversion + " " + build)
		return
	if os.name == 'nt':
		os.system("curl --silent -o lversion.txt https://raw.githubusercontent.com/EpicGamerCodes/PythonPrompt/master/lversion.txt --ssl-no-revoke")
	else:
		os.system("wget  -q -O lversion.txt https://raw.githubusercontent.com/EpicGamerCodes/PythonPrompt/master/lversion.txt")
		print("Lastest Version number downloaded from Github.")
	if os.path.isfile(appath + 'lversion.txt'):
		with open(appath + 'lversion.txt', 'r') as file:
			rlappversion = file.read().replace('\n', '')
		if lappversion == "":
			lappversion = rlappversion
			del rlappversion
	else:
		print("There was an error downloading the Latest Version number from Github!")
	if ((lappversion == "404: Not Found") or (lappversion == "")):
		print("Error in getting latest version file.")
		print("Current Version will become latest")
		print("Putting in queue...")
		lappversion = "Could not get the lastest version."
	if os.path.isfile(appath + 'lversion.txt'):
		os.remove(appath + "lversion.txt")
	if startup:
		cls()
	return
	
def checkforupdate():
	global lappversion
	global appversion
	cls()
	if lappversion == "":
		version()
	if lappversion == "Could not get the lastest version.":
		print("Could not get the lastest available version!\nCurrent Version: " + appversion)
		print("Version Available: Error getting latest version")
		print("Press anything else to continue.")
		print("Action / function has been put in queue. (type queue /? for help)")
		if os.path.isfile(appath + 'modules/config/queue.ini'):
			with open(appath + 'modules/config/queue.ini', 'r+') as f:
				f.write("checkforupdate")
		cho = input("")
		return
	if appversion != lappversion:
		avr = appversion.split()[0]
		if avr == "Stable":
			nav = appversion[7:]
		elif avr == "Beta":
			nav = appversion[5:]
		elif avr == "Alpha":
			nav = appversion[6:]
		elif avr == "Pre-Alpha":
			nav = appversion[10:]
		else:
			nav = "9.9.9"
		# lappversion[7:] is currently removing "Pre-Alpha ", need to change on Stable
		if lappversion[7:] <= nav:
			print("Update Required.\nCurrent Version: " + appversion)
			print("Version Available: " + lappversion)
			print("\nPress L to download the latest version")
			print("Press anything else to continue.")
			cho = input("Option Here:")
			if cho == "L":
				webbrowser.open('https://github.com/EpicGamerCodes/PythonPrompt/releases', new = 2)
		else:
			print("Current Version is higher than available release.")
			ilog("Current Version is higher than available release.")
			if cav:
				print("Cause: Using custom App Version")
			else:
				if ((avr == "Pre-Alpha") or (avr == "Alpha") or (avr == "Beta")):
					print("Cause: Assuming using a " + avr + " Build")
					ilog("Cause: Assuming using a " + avr + " Build")
				else:
					print("Cause: Assuming using a Unlabled Build")
					ilog("Cause: Assuming using a Unlabled Build")
	else:
		print("You are currently on the latest version of PythonPrompt")
		return
		
def allvars():
    for k,v in uservar.items():
        print(k, v)
        
def title(text):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(text)
    else:
        print('\33]0;' + text + '\a', end='', flush=True)
        
def vol():
    cdrive = Path.home().drive
    print("Volume in drive " + cdrive)
    
def doqueue(force = False):
   if force:
   	print("Force running fuctions in the queue might cause some unexpected changes.")
   	print("Type C to continue (for testing/development purposes)")
   	print("Type anything else to exit")
   	cho = input(">>")
   	if ((cho == "C") or (cho == "c")):
   		pass
   	else:
   		return
   cls()
   print("Proccessing queue.ini...")
   print("This may take a moment")
   if os.path.isfile(appath + 'modules/config/queue.ini'):
	   with open(appath + 'modules/config/queue.ini', 'r') as file:
		   ttd = file.read().replace('\n', '')
   else:
    print("Failure.")
    print("queue.ini does not exist!")
    input("Press anything to return.")
    return
	
	#FIX THIS
def clearqueue(force = False):
   if force:
   	print("Force clearing fuctions in the queue might cause some unexpected changes.")
   	print("Type C to continue (for testing/development purposes)")
   	print("Type anything else to exit")
   	cho = input(">>")
   	if ((cho == "C") or (cho == "c")):
   		return
   	else:
   		pass
   cls()
   if os.path.isfile(appath + 'modules/config/queue.ini'):
   	open(appath + 'modules/config/queue.ini', 'w').close()
   else:
    print("Failure.")
    print("queue.ini does not exist!")
    input("Press anything to return.")
    return

def showqueue():
	with open(appath + 'modules/config/queue.ini', 'r'):
		print(f.read())
		
def dirc():
	files = os.listdir('.')
	for f in files:
		print(f)
		
def syscommands():
	cls()
	print("This feature allows you to run your System Command's in Python Prompt.")
	print("There are 2 modes: After and Before")
	print("\nBefore runs the command through the system before its ran through PythonPrompt.")
	print("This will cause your System commands to override PythonPrompt Commands, meaning you cant use the same commands")
	print("\nAfter runs the command through the system after its ran through PythonPrompt.")
	print("This will cause PythonPrompt Commands to override your System Commands, meaning you cant use the same commands")
	print("B/A/D (Before/After/Disabled)")
	cho = input(">")
	if ((cho == "B") or (cho == "b")):
		print("This feature will completely disable all PythonPrompt commands due to a bug.")
		cho = input("Continue? C/R (Continue/Return)")
		if ((cho == "C") or (cho == "c")):
			config['main']['syscommands'] = 'Before'
		if ((cho == "R") or (cho == "r")):
			return
	if ((cho == "A") or (cho == "a")):
		config['main']['syscommands'] = 'After'
	if ((cho == "D") or (cho == "d")):
		config['main']['syscommands'] = 'Disabled'
	cls()
	print("You need to restart PythonPrompt for these changes to take effect!")	
	with open(appath + 'modules/config/config.ini', 'w') as configfile:
		config.write(configfile)
		
def settings(dsettings = None):
	cls()
	if dsettings == "1":
		syscommands()
		return
	print("1) Enable System Commands")
	print("2+) WIP")
	print("R) Return")
	cho = input(">")
	if cho == "1":
		syscommands()
		lcls()
		return
	if ((cho == "R") or (cho == "r")):
		lcls()
		return
	else:
		print("Not a valid option!")
		
def currentbugs():
	print("The current bugs are:")
	print("syscommands: Before - disables all PythonPrompt commands")
	
def startf(file = False):
	if not file:
		print("A file was not specified!")
		return
	if os.path.isfile(os.getcwd() + "/" + file):
		if file[-3:] == ".py":
			os.system("python3 " + file)
			return
		if OS == "Windows":
			os.startfile(file)
		else:
			subprocess.call(['open', file])
	else:
		print("The file does not exist!")
		
def type(file = False):
	if not file:
		print("A file was not specified!")
		return
	if os.path.isfile(os.getcwd() + "/" + file):
		with open(os.getcwd() + "/" + file, "r") as f:
			print(f.read())
	else:
		print("The file does not exist!")

def sysinfo():
	print("="*40, "System Information", "="*40)
	uname = platform.uname()
	print(f"System: {uname.system}")
	print(f"Node Name: {uname.node}")
	print(f"Release: {uname.release}")
	print(f"Version: {uname.version}")
	print(f"Machine: {uname.machine}")
	print(f"Processor: {uname.processor}")

def renf(file = None, name = None):
	if ((file == None) or (name == None)):
		print("A file or a new file name was not specifed.")
	else:
		os.rename(file, name)
	
setfv2 = time.perf_counter()
ilog("Finished making functions.")
ilog("Checking for updates...")
cls()
setu1 = time.perf_counter()
if not forced:
	version(True)
	checkforupdate()

setu2 = time.perf_counter()
if not forced:
	ilog("Check complete! Current V: " + appversion + ", Lastest V: " + lappversion)
else:
	ilog("Current V: " + appversion + ", Latest V unknown (forced mode).")
cls()
set2 = time.perf_counter()

# Total Setup time
elsp = set2 - set1
selsp = str(round(elsp, 3))
ilog("Time taken to setup: " + selsp + " seconds.")

# Debug log setup time
elspd = setd2 - setd1
selspd = str(round(elspd, 6))
ilog("Setting up the debug log took: " + selspd + " seconds.")

# Detecting Operating System time
elspos = setos2 - setos1
selspos = str(round(elspos, 3))
ilog("Finding out the Operating System took: " + selspos + " seconds.")

# Setting up functions and varibles time
elspfv = setfv2 - setfv1
selspfv = str(round(elspfv, 6))
ilog("Setting up the fucntions and varibles took: " + selspfv + " seconds.")

# Checking for updates time
elspu = setu2 - setu1
selspu = str(round(elspu, 3))
ilog("Checking for updates took: " + selspu + " seconds.")

# Finding out which one took the longest
highest = max(elspd, elspos, elspfv, elspu)
if highest == elspd:
	ilog("Setting up the Debug log took the longest amount of time.")
elif highest == elspos:
	ilog("Finding out the Operating System took the longest amount of time.")
elif highest == elspfv:
	ilog("Setting up the functions and varibles took the longest amount of time.")
elif highest == elspu:
	ilog("Checking for updates took the longest amount of time.")
	
# Finding out which one took the shortest
low = min(elspd, elspos, elspfv, elspu)
if low == elspd:
	ilog("Setting up the Debug log took the smallest amount of time.")
elif low == elspos:
	ilog("Finding out the Operating System took the smallest amount of time.")
elif low == elspfv:
	ilog("Setting up the functions and varibles took the smallest amount of time.")
elif low == elspu:
	ilog("Checking for updates took the smallest amount of time.")
	
# Give warning if Total Setup time is over 5 seconds
if elsp >= 5:
	ilog("<<< Over 5 seconds were taken to setup. Abnormal activity detected! >>>")
	print("<<< Over 5 seconds were taken to setup. Abnormal activity detected! >>>")

# Deleting above varibles
del set1, set2, selsp, elsp
del setd1, setd2, selspd, elspd
del setos1, setos2, selspos, elspos
del setfv1, setfv2, selspfv, elspfv
del setu1, setu2, selspu, elspu
del highest, low

if not args.title == None:
	title(args.title)
ilog("Entered Command menu")
if os.path.isfile(appath + 'modules/config/history.txt'):
	with open(appath + 'modules/config/history.txt', 'w+') as f:
		f.write("\n")
if cap:
	print("<<< Using custom appath directory, Exprimental Feature in use! >>>")
	if fcap:
		print("<<< Custom appath directory does not exist! >>>")
if not os.path.isfile(appath + "/modules/config/config.ini"):
	print("<<< Configuration file does not exist. Default Values are being used. >>>")
if not fcap:
	os.chdir(appath)
print("This app is in Pre-Alpha and not ready for use yet.")
print("Only some commands work as of now.")
print("\nFor the command 'echo', varibles do not work. (To check varible contents use the command 'echovar')")
print("For a list of commands that are supported, use the command 'help'")
print('try start command on linux')
if message != "Disabled":
	print(message)
while True:
	#Asking for input
	code = ""
	code = input(os.getcwd() + ">")
	if code != "":
		if os.path.isfile(appath + 'modules/config/history.txt'):
			with open(appath + 'modules/config/history.txt', 'a+') as f:
				f.write("\n")
				f.write(code)
	#FIX
	if syscommand == "Before":
		os.system(code)
		code = ""
	if code == "cls":
		cls()
	elif code[0:7] == "echovar":
		echovar(code[8:])
	elif code[0:4] == "echo":
		echo(code[5:])
	elif code == "":
		continue
	elif code[0:8] == "settings":
		settings(code[9:])
		code = ""
	elif code[0:3] == "set":
		temp = code.split(" ")
		store = str(temp[2:])
		store = store.translate({ord(c): None for c in "'[],"})
		set(str(temp[1]), store)
		temp = ""
		store = ""
	elif code == "help":
		cls()
		help()
		print("\n")
	elif code == "help/inputs":
		cls()
		helpi()
		print("\n")
	elif code == "help/dev":
		cls()
		helpdev()
		print("\n")
	elif code == "help/debug":
		cls()
		helpdebug()
		print("\n")
	elif code[0:2] == "cd":
		cd(code[2:])
	elif code[0:6] == "delvar":
		name = code[7:]
		if name in uservar:
			del uservar[name]
			print(name + " varible has been deleted.")
		else:
			print("That varible does not exist!")
		del name
		code = ""
	elif code[0:3] == "del":
		delcmd(code[4:])
	elif code[0:5] == "mkdir":
		mkdir(code[6:])
	elif code[0:6] == "mkfile":
		mkfile(code[7:])
	elif code == "version":
		version()
	elif code == "versionup":
		version(force = True)
		version()
	elif code == "update":
		checkforupdate()
	elif code == "allvars":
		allvars()
	elif code[0:5] == "title":
		title(code[6:])
	elif code == "os":
		print(OS)
	elif ((code == "exit") or (code == "quit")):
		quit()
	elif code == "queue /?":
		slashqueue()
	elif code == "queue/clear":
		clearqueue(True)
	elif code == "queue/do":
		doqueue(True)
	elif code == "queue/show":
		showqueue()
	elif code == "restart":
		os.execv(sys.argv[0], sys.argv)
		quit()
	elif code == "currentbugs":
		currentbugs()
	elif ((code == "vol") or (code == "volume")):
		vol()
	elif ((code == "ls") or (code == "tree")):
		dirc()
	elif code == "history":
		if os.path.isfile(appath + 'modules/config/history.txt'):
			with open(appath + 'modules/config/history.txt', 'r') as f:
				print(f.read())
	elif code == "syscommands":
		syscommands()
	elif code[0:5] == "start":
		startf(code[6:])
	elif code[0:4] == "type":
		type(code[5:])
	elif code == "args":
	       print(' '.join(f'{k}={v}' for k, v in vars(args).items()))
	elif code == "sysinfo":
			sysinfo()
	elif code[0:3] == "wte":
			if code[4:] == "":
				wte()
			else:
				wte(code[4:])
	elif code[0:3] == "ren":
			try:
				code.split()[1]
				er = False
			except:
				print("You need to specify a file to rename!")
				er = True
			try:
				code.split()[2]
				er = False
			except:
				print("You need to specify text to rename the file!")
				er = True
			if not er:
				renf(code.split()[1], code.split()[2])
		
	# Debug Commands
	elif ((code == "debug.cls") or (code == "debug.clear")):
		open(appath + 'modules/config/logs/debug.log', 'w').close()
		print("debug.log was cleared")
	elif code == "debug.show":
		with open(appath + 'modules/config/logs/debug.log', 'r') as f:
			print(f.read())
	elif ((code == "debug_all.cls") or (code == "debug_all.clear")):
		open(appath + 'modules/config/logs/debug.log', 'w').close()
		open(appath + 'modules/config/logs/debug_s.log', 'w').close()
		print("All debug logs were cleared.")
	
	# Debug_s Commands
	elif ((code == "debug_s.cls") or (code == "debug_s.clear") or (code == "ds.clear") or (code == "ds.cls")):
		open(appath + 'modules/config/logs/debug_s.log', 'w').close()
		print("debug_s.log was cleared.")
	elif ((code == "debug_s.show") or (code == "ds")):
		with open(appath + 'modules/config/logs/debug_s.log', 'r') as f:
			print(f.read())
	
	# Duplicate Commands
	elif code[0:5] == "chdir":
		cd(code[5:])
	# After Commands
	elif syscommand == "After":
		os.system(code)
	else:
		print("Not a valid command!")
