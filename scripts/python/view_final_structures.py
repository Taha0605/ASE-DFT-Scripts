#! /usr/bin/env python3

import os

files = os.listdir('./')
for file in files:
	if 'structure' in file:
		subdirectories = os.listdir('./'+file)
		max = 1
		for dir in subdiretories:
			i = dir[0]
			if i > max:
				max = i
		
