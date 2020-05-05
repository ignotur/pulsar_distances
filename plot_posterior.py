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


lib = cdll.LoadLibrary('./d_post.so')
lib.post_d.restype = ctypes.c_double

## Example for PSR J0218+4232

gl = 139.51
gb = -17.53
varpi     = 0.16    ## mas
varpi_err = 0.09

d = np.linspace (0.01, 10, 100) ## range of possible distances
post_d = []

for i in range (0, len(d)):

	l          = c_double (gl)
	b          = c_double (gb)
	di         = c_double (d[i])
	varpi_     = c_double (varpi)
	varpi_err_ = c_double (varpi_err)

	post_d_res = lib.post_d (di, varpi_, varpi_err_, l, b)
	post_d.append (post_d_res)

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

plt.plot (d, post_d / np.max(post_d))
plt.xlabel ('D (kpc)')
plt.ylabel ('Relative probability')
plt.show()


