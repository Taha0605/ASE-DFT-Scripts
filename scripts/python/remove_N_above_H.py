## To remove those structure where the H atoms are pointing towards the BHT instead of the N atom, which should be the one adsorbing on the BHT.
import os
from ase.io import read
from ase import atoms

files = os.listdir('./')

for file in files:
	if not '.traj' in file:
		continue
	atoms = read(file)
	
