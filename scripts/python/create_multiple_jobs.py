#! /usr/bin/env python3
## This file reads a directory full of .traj files and one copy each of a run.py, vasp.sh amd job.json files and ..
## .. creates different job directories for each .traj file with the run.py file being configured for that ..
## .. particular one
import os
files = os.listdir('./')
for i in range(len(files)):
	file = files[i]
	if 'traj' in file:
		new_directory_name = str(i+1)+'structure'
		os.mkdir(new_directory_name)
		runpy_file = open('run.py', 'r')
		data = runpy_file.readlines()
		for j in range(len(data)):
			if 'io.read' in data[j]:
				line_index = j
		data[line_index] = 'atoms = io.read("./'+file+'")\n'
		runpy_file.close()
		runpy_file = open('run.py', 'w')
		runpy_file.writelines(data)
		runpy_file.close()
		os.mkdir(new_directory_name+'/1calc')
		os.popen('cp run.py vasp.sh ./'+new_directory_name+'/1calc')
		os.rename('./'+file, './'+new_directory_name+'/1calc/'+file)

