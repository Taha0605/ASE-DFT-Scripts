#! /usr/bin/env python3
import os
import sys

files = os.listdir('./')
particular = sys.argv[1]
target_directory = sys.argv[2]

for file in files:
	if particular in file:
		os.system('mv '+file+' '+target_directory)
