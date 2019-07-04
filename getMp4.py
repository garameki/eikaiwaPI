#user/bin/env python
# -*- coding: utf-8 -*-


# get daily MP4 file from localhost
#
# usage : python3 getMp4.py 2019_06_25
# if the argument is not typed , the file name to get becomes the current date instead, for example, 2019_07_04.mp4

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


import urllib.request
from datetime import datetime

print(len(sys.argv))

filename = ""
if(len(sys.argv) == 2):
	filename = sys.argv[1] + ".mp4"
else:
	today = datetime.now()
	year = str(today.year)
	month = ("0"+str(today.month))[-2:]
	date = ("0"+str(today.day))[-2:]
	filename = year+"_"+month+"_"+date + ".mp4"


link = "http://192.168.3.2/git/eikaiwa/oto/" + filename
print("file name : " + filename)
print("link : " + link)
urllib.request.urlretrieve(link,"oto/" + filename)
print("完了しました")

