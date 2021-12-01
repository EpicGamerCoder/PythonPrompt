import os, logging, time, sys
from time import gmtime, strftime

f = open("modules/config/logs/debug_s.log", "a")
f.write("\n------------------------------------------------------\n\n")
f.close()

def ilog(text = "Something happend, but no text was defined. Please check for a undefined ilog()!"):
  logtime = strftime("%H:%M:%S", gmtime())
  logdate = strftime("%Y-%m-%d", gmtime())
  f = open("modules/config/logs/debug_s.log", "a")
  f.write("[" + logdate + "]" + " " + logtime + " - " + text + "\n")
  if text == "exit":
    f.write("------------------------------------------------------\n")
  if text == "clear":
    f.close()
    os.remove("modules/config/logs/debug_s.log")
    open("modules/config/logs/debug_s.log", 'w').close()
  f.close()
