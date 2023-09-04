#! /usr/bin/env python3

import os
import sys
directory_name = sys.argv[1]
current_directory = os.getcwd()
entries = os.listdir(current_directory)
max = 0
for entry in entries:
	if entry[1:len(entry)] == directory_name:
		if int(entry[0]) > max:
			max = int(entry[0])

directory_name = str(max+1) + directory_name
os.mkdir(directory_name)
