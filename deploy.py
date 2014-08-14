#!/usr/bin/env python

import os
import subprocess
import fileinput
import re


subprocess.call(["grunt", "build"])
subprocess.call(["rm", "js/core.min.js"])
subprocess.call(["cp", "views/base.html", "views/base.tmp.html"])


f = open('views/base.html','r')
filedata = f.read()
f.close()

newdata = re.sub(r'{# dev #}.*?{# enddev #}', '<script src="/js/site.min.js"></script>', filedata, 1, re.S)

f = open('views/base.html','w')
f.write(newdata)
f.close()


os.chdir("../")
subprocess.call(["appcfg.py", "update", "patchsheet"])
os.chdir("patchsheet")

subprocess.call(["mv", "views/base.tmp.html", "views/base.html"])
