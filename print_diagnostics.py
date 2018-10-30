#!/usr/bin/python
######################################################################
# Name:         read_Architect_bin_section.py
# Author:        A. Marocchino
# Date:			  2016-11-10
# Purpose:     Script Manger for binary file reader of Architect
# Source:       Python
#####################################################################

### loading shell commands
import numpy as np
from diagnostic_functions import *
### --- ###


def print_bunch_quality(x,y,z,px,py,pz,w):
	print('\n')
	print('{} {:7.3f} {}'.format('sx =', sigma(x,w), '(um)'))
	print('{} {:7.3f} {}'.format('sy =', sigma(y,w), '(um)'))
	print('{} {:7.3f} {}'.format('sz =', sigma(z,w), '(um)'))
	print('\n')
	print('{} {:7.3f} {}'.format('ex =', emittance(x,px,w), ' (mm-mrad)'))
	print('{} {:7.3f} {}'.format('ey =', emittance(y,py,w), ' (mm-mrad)'))
	print('\n')
	print('{} {:7.3f} {}'.format('dg/g (%) = ', energy_spread(px,py,pz,w)*100., ' (1)'))
