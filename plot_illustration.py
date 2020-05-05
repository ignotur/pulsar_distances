from math import *
import numpy as np
import ctypes
from ctypes import cdll, c_double
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rc('font', family='serif')
mpl.rcParams.update({'font.size': 12})
mpl.rcParams.update({'legend.labelspacing':0.25, 'legend.fontsize': 12})
mpl.rcParams.update({'errorbar.capsize': 4})

### Program to estimate the posterior distance given parallax
### This program can be found at https://github.com/ignotur/pulsar_distances 
### Written by Andrei Igoshev (ignotur@gmail.com)


## Linking the C++ library
lib = cdll.LoadLibrary('./d_post.so')
lib.post_d.restype = ctypes.c_double
lib.cnd_varpi.restype = ctypes.c_double
lib.int_d.restype = ctypes.c_double

###########################################
## Example for PSR J0218+4232
## Enter here measurements for radio pulsar

gl = 139.51         ## Galactic longitude and latitude
gb = -17.53
varpi     = 0.16    ## parallax [mas]
varpi_err = 0.09    ## parallax error [mas]

###########################################

d = np.linspace (0.01, 10, 100) ## range of distances
post_d = []

cnd_p   = []
prior_p = []

for i in range (0, len(d)):

	l          = c_double (gl)
	b          = c_double (gb)
	di         = c_double (d[i])
	varpi_     = c_double (varpi)
	varpi_err_ = c_double (varpi_err)

	post_d_res = lib.post_d (di, varpi_, varpi_err_, l, b) ## This function returns the posterior
	post_d.append (post_d_res)                             ## This list will contain the values of the posterior for each distance

	cnd_v = lib.cnd_varpi (varpi_, varpi_err_, di)

	## int_d function requires l and b in radians in contrast to post_d function
	l          = c_double (radians(gl))
	b          = c_double (radians(gb))

	prior_v = lib.int_d (di, l, b)

	cnd_p.append   (cnd_v)
	prior_p.append (prior_v)

## Here I compute some useful statistics such as the location of the postrior maximum and credible range.

print ('Maximum of the posterior is at: ', round(d[np.argmax(post_d)], 2), ' kpc')
cum_post = np.cumsum(post_d) / np.sum(post_d)
lflag = False
rflag = False
for i in range (0, len(cum_post)):

	if (cum_post[i] >= 0.025) and (lflag == False):

		cil = d[i]
		lflag = True

	if (cum_post[i] >= 0.975) and (rflag == False):

		cir = d[i]
		rflag = True


print ('95% C.I. ranges from ', round(cil, 2), ' to ', round(cir, 2), ' kpc')

plt.plot (d, cnd_p / np.max(cnd_p), 'r--', label=r'$g_D (\varpi | D)$')
plt.plot (d, prior_p / np.max(prior_p), 'b:', label=r'$f_D (D)$')
plt.plot (d, post_d / np.max(post_d), 'k-', label=r'$P_D (D | \varpi)$')
plt.legend()
plt.xlabel ('D (kpc)')
plt.ylabel ('Relative probability')
plt.savefig('illustration.png')
plt.show()


