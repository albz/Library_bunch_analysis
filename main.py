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
x,y,z,px,py,pz,w = read_bunch_PS(path,'Elpout04.bin')
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('gamma',15,5e3,x,y,z,px,py,pz,w)
xs,ys,zs,pxs,pys,pzs,ws = particle_selector('slice',225.5,1e4,xs,ys,zs,pxs,pys,pzs,ws)

#--- plots ---#
plot_dots(zs,pzs,w)
plot_scatter(zs,pzs,w)

#--- print ---#
print_bunch_quality(xs,ys,zs,pxs,pys,pzs,ws)
