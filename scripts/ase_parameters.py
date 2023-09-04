from ase.io.trajectory import Trajectory
import sys

filename = sys.argv[1]
traj = Trajectory(filename)
for atoms in traj:
    print(atoms)
    atoms.pbc = (True, True, True)
    print(atoms.pbc)
    atoms.write(filename.split('.')[0]+'1.'+filename.split('.')[1])

traj.close()

# # dyn is the dynamics (e.g. VelocityVerlet, Langevin or similar)
# dyn.attach(traj.write, interval=100)
# dyn.run(10000)
# traj.close()