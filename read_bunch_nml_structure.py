#!/usr/bin/python
######################################################################
# Name:         read_bunch_PS_ALaDyn.py
# Author:       A. Marocchino
# Date:         18-03-2018
# Purpose:      In 'Lybrary_bunch_Analysis' read the phase space written with a namelist structure
# Source:       Python
#####################################################################

### loading libraries
import os
import numpy as np
### --- ###



# - #
def read_bunch_nml_structure(file_path,file_name):
	file = open(os.path.join(file_path,file_name))

	check_file_consistency=True
	if( isinstance( file.readline(), str)        == False): check_file_consistency=False
	try: 
		charge=float(file.readline())
	except:
		check_file_consistency=False
	if( isinstance( file.readline(), str)        == False): check_file_consistency=False
	try: 
		conversion=int(file.readline())
	except:
		check_file_consistency=False
	if( isinstance( file.readline(), str)        == False): check_file_consistency=False

	#--- file conforms to standard architect namelist structure ---#
	if( check_file_consistency == True):
		x,y,z,px,py,pz = np.loadtxt(file, delimiter='\t').transpose()
		w              = np.ones(x.shape) * charge/x.shape

	file.close()

	return x,y,z,px,py,pz,w
