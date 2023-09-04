#! /usr/bin/env python3

import os

files = os.listdir('./')
for file in files:
	print(file+'-')
	subs = os.listdir('./'+file)
	max1 = 1
	for sub in subs:
		if int(sub[0]) > max1:
			max1 = int(sub[0])
	os.system('cat '+file+'/dftu_structure/'+str(max1)+'calc/out.txt')
	os.system('cat '+file+'/dftu_structure_vib/'+str(max1)+'calc_vib/free_energy.log')
