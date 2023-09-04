#! /usr/bin/env/ python3
import os

files = os.listdir('./')

for file in files:
	if 'structure' in file:
		os.system('cp run.py '+file+'/1calc')
		runpy_file = open(file+'/1calc/run.py', 'r')
		data = runpy_file.readlines()
		line_index = 5
		filenames = os.listdir('./'+file+'/1calc/')
		filename = '.traj'
		for fname in filenames:
			if '.traj' in fname:
				filename = fname
		data[5] = 'atoms = io.read("./'+filename+'")'
		print(data[5])
		runpy_file.close()
		runpy_file = open(file+'/1calc/run.py', 'w')
		runpy_file.writelines(data)
		print('done')
		runpy_file.close()
		
