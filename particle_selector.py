#!/usr/bin/python
######################################################################
# Name:         particle_selector.py
# Author:       A. Marocchino, S. Romeo
# Date:
# Purpose:      In 'Lybrary_bunch_Analysis' select particle to analize
# Source:       Python
#####################################################################

### loading shell commands
import numpy as np
### --- ###

### --- select strategy --- ###
def particle_selector(strategy,Zmin,Zmax,X,Y,Z,Px,Py,Pz,W):

    if strategy == 'slice':
        particle_selector_slice(Zmin,Zmax,X,Y,Z,Px,Py,Pz,W)

### --- END select strategy --- ###



def particle_selector_slice(Zmin,Zmax,X,Y,Z,Px,Py,Pz,W):
    selected = np.asarray(Z>=z_min) & np.asarray(Z<=z_max)
    X, Y, Z  = X[selected], Y[selected], Z[selected]
    Px,Py,Pz =Px[selected],Py[selected],Pz[selected]
    W = W[selected]
    return X,Y,Z,Px,Py,Pz,W
