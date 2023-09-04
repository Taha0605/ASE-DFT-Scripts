from ase.io import read
atoms = read('final.traj')

a = atoms.get_magnetic_moments()

atoms1 = read('relaxed-Co-BHT.traj')

atoms1.set_initial_magnetic_moments(a)
atoms1.write('relaxed-Co-BHT1.traj')
