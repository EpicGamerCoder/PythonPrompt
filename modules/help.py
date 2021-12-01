def help():
    print("This is a python script that allows you to use Command Prompt commands in python.\nIn a future version, .bat / .cmd files will be supported too!")
    print("\nCommands:")
    print("echo [text] - Displays [text] on screen")
    print("echovar [varible name] - Displays content of varible with the name [varible name]")
    print("set [varible name] [varible content]- Creates a varible with its name being [varible name] and content being [varible content] (content can be accessed with 'echovar' command)")
    print("cd [directory] - Changes directory to [directory] (to goto drive root folder, use 'cd\\' command)")
    print("cls - Clears the screen")
    print("help - Shows this message")
    print("del [file / folder name] - Deletes [file / folder name]")
    print("mkdir [folder name] - Makes a folder with the name [folder name]")
    print("mkfile [file name] - Makes a file with the name [file name]")
    print("version - Get the current and latest app version")
    print("update - Checks for update using version.txt (stored on Github)")
    print("allvars - Shows all user varibles names and content")
    print("currentbugs - Shows the current bugs in PythonPrompt")
    print("volume - Shows the current volume label")
    print("tree - Displays the folder content of the current drive or path.")
    print("history - Shows command history")
    print("args - Shows the arguments passed to PythonPrompt")
    print("syscommands - Run your System's Commands in Python Prompt.")
    print("start - Start a file with its default program")
    print("type - Display a file's contents")
    print("\nDuplicate Commands:")
    print("chdir [directory] - Changes directory to [directory] (to goto drive root folder, use 'chdir\\' command)")
    print("allvars - Shows all user varibles names and content")
    print("delvar [varible name] -  Deletes varible with the name [varible name]")
    print("vol - Shows the current volume label")
    print("\nHelp Tips:")
    print("help/inputs - Shows the diffrent input flags")
    print("help/dev - Shows more commands intended for developing usage. These commands may cause errors if used incorrectly!")
    print("help/debug - Shows the info and commands used for the debug logs")
    return

def helpi():
	print(">>> - Criticality Important Message / Input")
	print(">> - Important Message / Input")
	print("> - Standard Message / Input")

def helpdev():
	print("versionup - Force re-checks the Latest Version number on Github")

def helpdebug():
    print("debug.log - This log stores all tge text that has been printed on the screen. The log gets cleared every time PythonPrompt restarts.")
    print("debug_s.log - This log stores any crucial infomation, if any errors and/or unusual behaviour is found, it will be stored in the log. This log is never cleared.")
    print("\nCommands:")
    print("debug.cls - Clears debug.log")
    print("debug_all.cls - Clears all debug logs")
    print("debug_s.cls - Clears debug_s.log")
    print("debug_s.show - Displays the debug_s.log")
    print("\nDuplicate Commands:")
    print("debug.clear - Clears debug.log")
    print("debug_all.clear - Clears all debug logs")
    print("debug_s.clear >|")
    print("ds.clear      >|")
    print("ds.cls         |< Clears debug_s.log")