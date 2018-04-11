#!/usr/bin/python
######################################################################
# Author:       A. Marocchino
# Date:
# Purpose:      plot sliced analisys
# Source:       python
#####################################################################

### loading shell commands
import os, os.path
import scipy
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import pylab as pyl

#--- load libraries: read Architect format --- #
# sys.path.append(os.path.join(os.path.expanduser('~'),'Codes','Code_Architect','Architect','utils','python_utils','architect_graphycal_unit'))
# from read_architect_bin import *

#--- load libraries: Library_Bunch_Analisys --- #
from diagnostic_functions import *
from particle_selector import *
from read_bunch_PS_master import *
from print_diagnostics import *
from plot_phase_space import *

#--- load libraries: plot_utility --- #
# plt.style.use(os.path.join(os.path.expanduser('~'),'Codes','Python_general_controllers','python_plot','plot_style_ppth.mplstyle'))
### --- ###


# --- path --- #
path = os.getcwd()

#--- main analisys ---#
x,y,z,px,py,pz,w = read_bunch_PS(os.path.join(path,'N'),'Elpout08.bin')

#--- select ionized particle by weight ---#
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('weight',0.00,0.1,x,y,z,px,py,pz,w)
#xs,ys,zs,pxs,pys,pzs,ws = particle_selector('gamma',30.,70.0,xs,ys,zs,pxs,pys,pzs,ws)
#xs,ys,zs,pxs,pys,pzs,ws = particle_selector('slice',0.0,293.0,xs,ys,zs,pxs,pys,pzs,ws)
pyl.plot(z-np.mean(z),pz,'.')
pyl.plot(zs-np.mean(z),pzs,'.')


#--- plots ---#
#plot_scatter(zs,pzs,ws,'z','pz')
#plot_scatter(z,w,w,'z','w')

#--- print ---#
print_bunch_quality(xs,ys,zs,pxs,pys,pzs,ws)



#--- plot particle positions ---#
M=np.loadtxt(os.path.join(path,'N','rho_tot_y_03.txt'))
z=np.loadtxt(os.path.join(path,'N','x_03.txt'))
y=np.loadtxt(os.path.join(path,'N','y_03.txt'))
pyl.contourf(z,y,np.log10(M),10)
x,y,z,px,py,pz,w = read_bunch_PS(os.path.join(path,'N'),'Elpout03.bin')
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('weight',0.00,0.1,x,y,z,px,py,pz,w)
pyl.plot(z,x,'o',ms=.2)



M=np.loadtxt(os.path.join(path,'N','rho_tot_y_06.txt'))
z=np.loadtxt(os.path.join(path,'N','x_06.txt'))
y=np.loadtxt(os.path.join(path,'N','y_06.txt'))
pyl.contourf(z,y,np.log10(M),10)
x,y,z,px,py,pz,w = read_bunch_PS(os.path.join(path,'N'),'Elpout06.bin')
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('weight',0.00,0.1,x,y,z,px,py,pz,w)
pyl.plot(z,x,'.')

M=np.loadtxt(os.path.join(path,'N','rho_tot_y_07.txt'))
z=np.loadtxt(os.path.join(path,'N','x_07.txt'))
y=np.loadtxt(os.path.join(path,'N','y_07.txt'))
pyl.contourf(z,y,np.log10(M),10)
x,y,z,px,py,pz,w = read_bunch_PS(os.path.join(path,'N'),'Elpout07.bin')
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('weight',0.00,0.1,x,y,z,px,py,pz,w)
pyl.plot(z,x,'.')
pyl.show()



