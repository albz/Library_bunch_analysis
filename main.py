#!/usr/bin/python
######################################################################
# Author:       A. Marocchino
# Date:
# Purpose:      plot sliced analisys
# Source:       python
#####################################################################

#--- load packages ---#
import os, os.path, sys
import scipy
import numpy as np
import matplotlib
#matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import pylab as pyl

#--- load libraries: read Architect format --- #
# sys.path.append(os.path.join(os.path.expanduser('~'),'Codes','Code_Architect','Architect','utils','python_utils','architect_graphycal_unit'))
# from read_architect_bin import *

#--- load libraries:Library_bunch_analysis --- #
sys.path.append(os.path.join(os.path.expanduser('~'),'Codes','Library_bunch_analysis'))
from diagnostic_functions import *
from particle_selector import *
from read_bunch_PS_master import *
from print_diagnostics import *
from plot_phase_space import *

# --- path --- #
path = os.getcwd()

x,y,z,px,py,pz,w = read_bunch_PS(path,'Dbunch_10.nml')
print_bunch_quality(x,y,z,px,py,pz,w)

#--- select ionized particle by weight ---#
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('weight',0.00,0.1,x,y,z,px,py,pz,w)
#xs,ys,zs,pxs,pys,pzs,ws = particle_selector('gamma',30.,70.0,xs,ys,zs,pxs,pys,pzs,ws)
#xs,ys,zs,pxs,pys,pzs,ws = particle_selector('slice',0.0,293.0,xs,ys,zs,pxs,pys,pzs,ws)
pyl.plot(z-np.mean(z),pz,'.')
pyl.plot(zs-np.mean(z),pzs,'.')


#--- plots ---#
#plot_scatter(zs,pzs,ws,'z','pz')
#plot_scatter(z,w,w,'z','w')



