import os

def wte(cmd = None):
	if cmd == None:
		print("This is the 'Why does this exist' module.")
		print("Use this command like this:\nwte/[command name] e.g: wte/inum")
	if cmd == "inum":
		print("The number outputed by this command is the number that seperates diiffrent instances of PythonPrompt. If you get the same number 2 times, because there is a 1 in 1000000000 (1 with 9 0's) of getting that! This code is ussually used for debugiging purrposes.")
	if cmd == "extracommands":
		print("This module allows you to add your own commands to PythonPrompt. These commands cannot override default commands for security reasons.")