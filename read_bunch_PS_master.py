#!/usr/bin/python
######################################################################
# Name:         read_bunch_PS_master.py
# Author:       A. Marocchino
# Date:			18-03-2018
# Purpose:      In 'Lybrary_bunch_Analysis' identify the output and find the appropriate reader
# Source:       Python
#####################################################################

### loading libraries
import os
from read_bunch_PS_ALaDyn import *
### --- ###


# - #
def read_bunch_PS(dir_path,file_name):

	name, extension = os.path.splitext(file_name)

	if( name[0:7]=='PSBunch' or name[0:6]=='Elpout'):
		z =read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'x')
		x =read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'y')
		y =read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'z')
		pz=read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'px')
		px=read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'py')
		py=read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'pz')
		w =read_bunch_PS_ALaDyn_bycomponent(dir_path,file_name,'w')

	return x,y,z,px,py,pz,w
