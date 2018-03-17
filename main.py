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
sys.path.append(os.path.join(os.path.expanduser('~'),'Codes','Code_Architect','Architect','utils','python_utils','architect_graphycal_unit'))
from read_architect_bin import *

#--- load libraries: Library_Bunch_Analisys --- #
from diagnostic_functions import *
from particle_selector import *
# from rolling_slice import *

#--- load libraries: plot_utility --- #
# plt.style.use(os.path.join(os.path.expanduser('~'),'Codes','Python_general_controllers','python_plot','plot_style_ppth.mplstyle'))
### --- ###


# --- path --- #
path = os.getcwd()


#--- main analisys ---#
x,y,z,px,py,pz,w = read_bunch_PS('PSBunch04.bin')

# read PS file
# Xcut, Ycut, Zcut, Pxcut, Pycut, Pzcut, Wcut = particle_selector('slice',0,3,X,Y,Z,Px,Py,Pz,W)

# print at screen
# print_all_diagnostics(Xcut, Ycut, Zcut, Pxcut, Pycut, Pzcut, Wcut)
