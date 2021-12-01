import platform
import re

def volname(path):
    if platform.system() == "Darwin":
        return re.search("^\/Volumes\/[^/]+/", path).group(0)
    elif platform.system() == "Windows":
        return path()[0:3]