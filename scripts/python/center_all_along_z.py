import os
from ase.io import read
from ase import Atoms
import numpy as np
files = os.listdir('./')

for file in files:
	if '.traj' in file:
		atoms = read(file)
		pos = atoms.get_positions()
		disp = np.zeros(pos.shape)
		disp[:, 2] = 5
		pos = pos + disp
		atoms.set_positions(pos)
		atoms.write(file)
