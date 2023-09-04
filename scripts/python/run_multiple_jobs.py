#! /usr/bin/env python3

## This script runs sbatch vasp.sh for the latest calculation in job directory in the main directory - relevant


import os
directories = os.listdir('./')

cnt = 0
for i in range(len(directories)):
	directory = directories[i]
	if 'structure' in directory:
		subdirectories = os.listdir('./'+directory+'/')
		max = 1
		for j in range(len(subdirectories)):
			subdirectory = subdirectories[j]
			if int(subdirectory[0]) > max:
				max = int(subdirectory[0])
		current = str(i+1)
		max = str(max)
		path_to_file = './'+directory+'/'+max+'calc/vasprun.xml'
		file_exists = os.path.exists(path_to_file)
		if not file_exists:
			command = 'cd '+directory+'/'+max+'calc/; sbatch vasp.sh'
			os.system(command)


