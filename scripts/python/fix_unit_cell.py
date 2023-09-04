from ase.io import read
from ase import atoms
import sys

atoms = read(sys.argv[1])
cell = atoms.get_cell()
cell[2,2] = 25
atoms.set_cell(cell)
atoms.write(sys.argv[1])
