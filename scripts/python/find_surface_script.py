from ase.io import read,write
from ase.build import surface
import sys

# A=read('Ni-BHT.traj',format='traj')  ### format can be vasp.
# B=surface(A,(3,0,-1),1,vacuum=10)
# write('Ni-benzene-terminating.traj',B,format='traj')

filename = sys.argv[1]
print(sys.argv)
fileformat = filename.split('.')[1]
print(fileformat)
A = read(filename, format=fileformat)
miller_index = tuple(map(int, sys.argv[2].split(',')))
print(miller_index)
vacuum_set = int(sys.argv[3])
B = surface(A, miller_index, 1, vacuum=vacuum_set)

write(filename.split('.')[0]+"_surface."+fileformat, B, format=filename.split('.')[1])