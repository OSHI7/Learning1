import numpy as np
from py_pol import degrees
from py_pol.stokes import Stokes
from py_pol.mueller import Mueller
import random

V=Stokes('V')
V.from_elements(1, -1, 0, 0)

H=Stokes('H')
H.linear_light(angle=0, intensity=1)

random.randomint()