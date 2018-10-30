#!/usr/bin/python
######################################################################
# Name:         read_bunch_PS_master.py
# Author:       A. Marocchino
# Date:			18-03-2018
# Purpose:      In 'Lybrary_bunch_Analysis' identify the output and find the appropriate reader
# Source:       Python
#####################################################################

### loading libraries
import os, sys
sys.path.append(os.path.join(os.path.expanduser('~'),'Codes','Code_Architect','Architect','utils','python_utils','architect_graphycal_unit'))
from read_bunch_PS_ALaDyn import *
from architect_read_PS_bin import *
from read_bunch_nml_structure import *
### --- ###

# - #
def read_bunch_PS(file_path,file_name):

	name, extension = os.path.splitext(file_name)

	if( name[0:7]=='PSBunch' or name[0:6]=='Elpout'):
		z =read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'x')
		x =read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'y')
		y =read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'z')
		pz=read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'px')
		px=read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'py')
		py=read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'pz')
		w =read_bunch_PS_ALaDyn_bycomponent(file_path,file_name,'w')


	if( extension=='.arch'):
		architect_read_PS_bin_v_3(os.path.join(file_path,'out','PS'),file_name)
		x, y, z = var.x, var.y, var.z
		px, py, pz = var.px, var.py, var.pz
		w=var.macro_particle_nume
		# w=np.ones(len(x))
		var.x=0; var.y=0; var.z=0
		var.px=0; var.py=0; var.pz=0
		var.macro_particle_nume=0

	if( extension=='.nml'):
		x,y,z,px,py,pz,w = read_bunch_nml_structure(file_path,file_name)


	return x,y,z,px,py,pz,w
