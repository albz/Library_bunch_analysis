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


def print_all_diagnostics(x,y,z,px,py,pz,w):
	print('\n')
	print('sx = ',sigma(x,w),' (um)')
	print('sy = ',sigma(y,w),' (um)')
	print('sz = ',sigma(z,w),' (um)')
	print('\n')
	print('ex = ',emittance(x,px,w),' (mm-mrad)')
	print('ey = ',emittance(y,py,w),' (mm-mrad)')
	print('\n')
	print('dg/g = ',energy_spread(px,py,pz,w),' (1)')
