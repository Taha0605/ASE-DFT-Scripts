import numpy as np
from ase.io import read
from ase import Atoms
from math import pi, sqrt

atoms = read('translated-Ni-BHT.traj')


def translate_to_center(atoms):
    # unit_cell_params = Atoms.get_cell_lengths_and_angles(atoms)
    # print(unit_cell_params)
    positions = atoms.get_positions()
    positions = np.array(positions)
    corner_atom = positions[21]
    displacement_x = corner_atom[0]
    displacement_y = corner_atom[1]
    displacement_z = corner_atom[2]
    displacement_array = np.zeros((30, 3))
    displacement_array[:, 0] = displacement_x
    displacement_array[:, 1] = displacement_y
    displacement_array[:, 2] = displacement_z
    positions = positions - displacement_array
    return positions

#new_positions = translate_to_center(atoms)
new_positions = atoms.get_positions()
new_atoms = atoms


tags = atoms.get_tags()
print(tags)

coord1 = np.array([14.511, (new_positions[13, 1]+new_positions[14, 1])/2.0, 1.746])
# Change the ones below
coord2 = np.array([(new_positions[28, 0]+new_positions[29, 0])/2.0, 0, 1.95])
coord3 = np.array([0, (new_positions[12, 1]+new_positions[15, 1])/2.0, 1.919])
new_origin_x = (new_positions[28, 0]+new_positions[29, 0])/2.0
new_origin_z = new_positions[28, 2]


# print(coord1)
# print(coord2)
# print(coord3)
displacement_array = np.zeros((30,3))
displacement_array[:, 0] = new_origin_x
displacement_array[:, 2] = new_origin_z
new_positions = new_positions - displacement_array
new_atoms.set_positions(new_positions)
print(new_positions)

a = coord1 - coord2
b = coord3 - coord2
c = np.array([0, 0, 10])

print(a)
print(b)
print(c)

new_atoms.pbc = (True, True, True)

new_atoms.write('modified-unit-cell-Ni-BHT.traj')

