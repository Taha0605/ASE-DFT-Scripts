#! /usr/bin/env python3

## This script checks the force convergence of the directories and restarts the calculations if the calculations ..
## .. didn't converge

import os
from ase.io import read
from ase import Atoms
from numpy.linalg import norm

directories = os.listdir('./')

for i in range(len(directories)):
	directory = directories[i]
	subdirectories = os.listdir('./'+directory+'/')
	max = 1
	for j in range(len(subdirectories)):
		subdirectory = subdirectories[j]
		if int(subdirectory[0]) > max:
			max = int(subdirectory[0])
	current = str(i+1)
	max = str(max)
	path_to_file = './'+directory+'/'+max+'calc/out.txt'
	out_txt_file_exists = os.path.exists(path_to_file)
	if not out_txt_file_exists:
		atoms = read('./'+directory+'/'+max+'calc/vasprun.xml')
		e = atoms.get_potential_energy()
		f = norm(max(atoms.get_forces(), key=norm))
		data = []
		data.append('final energy '+str(e)+'\n')
		data.append('max force '+str(f)+'\n')
		file = open(path_to_file, 'w')
		file.writelines(data)
		file.close()
	path_to_traj_file = './'+directory+'/'+max+'calc/final.traj'
	final_traj_file_exists = os.path.exists(path_to_traj_file)
	if not final_traj_file_exists:
		atoms = read('./'+directory+'/'+max+'calc/vasprun.xml')
		atoms.write('final.traj')
		del atoms
	file = open(path_to_file, 'r')
	data = file.readlines()
	final_energy = float(data[0][14:22])
	force = float(data[1][10:16])
	file.close()
	print(directory+'/'+max+'calc - final energy = '+str(final_energy))
	print(directory+'/'+max+'calc - max force = '+str(force))
	if force <= 0.01:
		print(path_to_file+' - converged')
	else:
		new_max = str(int(max)+1)
		os.system('cd '+directory+'/; mkdir '+new_max+'calc')
		os.system('cd '+directory+'/'+max+'calc/; cp final.traj run.py vasp.sh job.json ../'+new_max+'calc/')
		os.system('mv '+directory+'/'+new_max+'calc/final.traj '+directory+'/'+new_max+'calc/repeat.traj')

		runpy_file = open(directory+'/'+new_max+'calc/run.py', 'r')
		data = runpy_file.readlines()
		for j in range(len(data)):
			if 'io.read' in data[j]:
                               	line_index = j
		data[line_index] = 'atoms = io.read("./repeat.traj")\n'
		runpy_file.close()
		runpy_file = open(directory+'/'+new_max+'calc/run.py', 'w')
		runpy_file.writelines(data)
		runpy_file.close()

