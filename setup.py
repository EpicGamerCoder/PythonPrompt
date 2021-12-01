from distutils.core import setup
import py2exe 
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

setup(console=['main.py'])