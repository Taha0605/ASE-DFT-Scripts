from ase.io import read
from ase import Atoms
import numpy as np
import sys

atoms = read(sys.argv[1])
positions = atoms.get_positions()
disp = np.zeros(positions.shape)
disp[:, 2] = 5
positions = positions + disp
atoms.set_positions(positions)
atoms.write('repeat.traj')
