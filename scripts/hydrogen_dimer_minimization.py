from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np
d = 2
# t = np.pi / 180 * 104.51
hydrogen_dimer = Atoms('H2',
              positions=[(d, 0, 0),
                         (0, 0, 0)],
              calculator=EMT())
dyn = BFGS(hydrogen_dimer, trajectory='test.traj', restart = 'test.pckl')
dyn.run(fmax=0.05)
