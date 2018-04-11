#!/usr/bin/python
######################################################################
# Name:         read_Architect_bin_section.py
# Author:        A. Marocchino
# Date:			  2016-11-10
# Purpose:     Script Manger for binary file reader of Architect
# Source:       Python
#####################################################################

### loading shell commands
import numpy as np
### --- ###

def mean(x,w):
	mu=np.average(x,weights=w)
	return mu

def sigma(x,w):
	mu=mean(x,w)
	sigma=np.sqrt( np.average((x-mu)**2, weights=w) )
	return sigma

def covariance(x,px,w):
	mu_x=mean(x,w)
	mu_px=mean(px,w)
	covariance=np.average((x-mu_x)*(px-mu_px), weights=w)
	return covariance

def emittance(x,px,w):
	sigma_x = sigma(x,w)
	sigma_px = sigma(px,w)
	cov_x_px = covariance(x,px,w)
	emittance = np.sqrt( sigma_x**2*sigma_px**2-cov_x_px**2);
	return emittance

def energy_spread(px,py,pz,w):
	gamma = np.array(np.sqrt(1. + px**2 + py**2 + pz**2))
	mu_gamma=np.average(gamma,weights=w)
	sigma_gamma=np.sqrt( np.average((gamma-mu_gamma)**2, weights=w) )
	en_spread = sigma_gamma/mu_gamma
	return en_spread

def alpha(x,px,py,pz,w):
	cov=covariance(x,px,w)
	eps=emittance(x,px,w)
	return -cov/eps
