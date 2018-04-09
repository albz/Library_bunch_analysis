#!/usr/bin/python
######################################################################
# Name:         plot_phase_space.py
# Author:       A. Marocchino
# Date:			2018-03-18
# Purpose:      plot the different component of the phase space
# Source:       Python
#####################################################################

### loading shell commands
import numpy as np
import pylab as pyl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
### --- ###


def plot_dots(x,y,w,*args):
	fig,ax1 = plt.subplots(1, figsize=(3.25,3.0))
	ax1.plot(x,y,'o',markersize=1)
	if(len(args)==2):
		ax1.set_xlabel(args[0])
		ax1.set_ylabel(args[1])
	pyl.show()

def plot_scatter(x,y,w,*args):
	size=3*w/np.max(w)
	fig,ax1 = plt.subplots(1, figsize=(3.25,3.0))
	ax1.scatter(x,y,s=size)
	if(len(args)==2):
		ax1.set_xlabel(args[0])
		ax1.set_ylabel(args[1])
	pyl.show()
