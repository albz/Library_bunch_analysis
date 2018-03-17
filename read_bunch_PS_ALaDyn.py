#!/usr/bin/python
######################################################################
# Name:         read_bunch_PS_ALaDyn.py
# Author:       A. Marocchino
# Date:         18-03-2018
# Purpose:      In 'Lybrary_bunch_Analysis' read the ALaDyn Phase Space
# Source:       Python
#####################################################################

### loading libraries
import os
import struct
import numpy as np
### --- ###



# - #
def read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,component):

	path     = os.path.join(dir_path,file_name)
	f        = open(path,'rb')
	cmp = []
	while True:
		try:
			Np=struct.unpack('i', f.read(4))
		except struct.error:
			#print "End of File"
			break
		vars=[]

		try:
			pass
			for i in range(0,Np[0]):
				vars=struct.unpack('ffffffff', f.read(4*8))
				if(component == 'x'): 	cmp.append(vars[0])
				if(component == 'y'): 	cmp.append(vars[1])
				if(component == 'z'): 	cmp.append(vars[2])
				if(component == 'px'): 	cmp.append(vars[3])
				if(component == 'py'): 	cmp.append(vars[4])
				if(component == 'pz'): 	cmp.append(vars[5])
				if(component == 'w'): 	cmp.append(vars[6])
				if(component == 'q'): 	cmp.append(vars[7])
		except:
			pass
	f.close()

	return np.array(cmp)
