#! /usr/bin/env python3

import os

files = os.listdir()

for file in files:
	if 'relevant' in os.listdir(file):
		os.system('cd '+file+'/relevant; mkdir 1calc')
		os.system('cd '+file+'/relevant/dftu; mv * ../1calc')
		os.system('cd '+file+'/relevant/; mv 1calc dftu')

	else:
		os.system('cd '+file+'; mkdir 1calc')
		os.system('cd '+file+'/dftu; mv * ../1calc')
		os.system('cd '+file+'/; mv 1calc dftu')
