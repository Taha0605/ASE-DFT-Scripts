import os

files = os.listdir('./')

os.system('rm .*')
os.system('rm */.*')
os.system('rm */calculation.json')
os.system('rm */*/.*')
os.system('rm */*/job.json')

i = 1
for file in files:
	if file == 'rename.py':
		continue
	subdirectory = os.listdir('./'+file)
	os.system('mv '+file+'/'+subdirectory[0]+' '+file+'/1calc')
	os.system('mv '+file+' '+str(i)+'structure')
	i += 1
