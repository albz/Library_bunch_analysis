#!/usr/bin/python
######################################################################
# Name:         particle_selector.py
# Author:       A. Marocchino
# Date:
# Purpose:      In 'Lybrary_bunch_Analysis' select particle to analyse
# Source:       Python
#####################################################################

### loading shell commands
import numpy as np
### --- ###

### --- select strategy --- ###
def particle_selector(strategy,value_min,value_max,x,y,z,px,py,pz,w):

    if strategy == 'slice':
        x,y,z,px,py,pz,w=particle_selector_slice(value_min,value_max,x,y,z,px,py,pz,w)

    if strategy == 'gamma':
        x,y,z,px,py,pz,w=particle_selector_gamma(value_min,value_max,x,y,z,px,py,pz,w)

    if strategy == 'iris':
        x,y,z,px,py,pz,w=particle_selector_iris(value_min,value_max,x,y,z,px,py,pz,w)

    return x,y,z,px,py,pz,w

### --- END select strategy --- ###



def particle_selector_slice(z_min,z_max,x,y,z,px,py,pz,w):
    selected = np.asarray(z>=z_min) & np.asarray(z<=z_max)
    x, y, z  = x[selected], y[selected], z[selected]
    px,py,pz =px[selected],py[selected],pz[selected]
    w = w[selected]
    return x,y,z,px,py,pz,w


def particle_selector_gamma(gamma_min,gamma_max,x,y,z,px,py,pz,w):
    gamma = np.sqrt(1.+px**2+py**2+pz**2)
    selected = np.asarray(gamma>=gamma_min) & np.asarray(gamma<=gamma_max)
    x, y, z  = x[selected], y[selected], z[selected]
    px,py,pz =px[selected],py[selected],pz[selected]
    w = w[selected]
    return x,y,z,px,py,pz,w

def particle_selector_iris(radius_min,radius_max,x,y,z,px,py,pz,w):
    radius_min=np.maximum(radius_min,0.)
    selected = np.asarray(x**2+y**2>=radius_min**2) & np.asarray(x**2+y**2<=radius_max**2)
    x, y, z  = x[selected], y[selected], z[selected]
    px,py,pz =px[selected],py[selected],pz[selected]
    w = w[selected]
    return x,y,z,px,py,pz,w
