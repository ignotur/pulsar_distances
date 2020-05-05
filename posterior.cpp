#include <cmath>
#include <iostream>
#include <cstdlib>

using namespace std;

extern "C" double cnd_varpi (double, double, double);
extern "C" double int_d (double, double, double);
extern "C" double post_d (double, double, double, double, double);

// Library to compute the posterior distance distribution given measured parallax (varpi)
// parallax error (sigma_varpi) and pulsar galactic coordinates. The coordinates
// are used in the prior.
// Combined using modules from pulsar velocity project by Dr Andrei Igoshev (ignotur@gmail.com)
// Arguments are as following: 
// D     - distance where the conditional probability needs to be estimated. [D] = [kpc]
// varpi - measured parallax of the pulsar. [varpi] = [mas]
// sigma_varpi - standard deviation of the parallax measurement. [sigma_varpi] = [mas]
// l, b  - Galactic longuitude and latitude of the pulsar. [l], [b] = [degrees]  

double post_d (double D, double varpi, double sigma_varpi, double l, double b) {

double res;

	l = l / 180. * M_PI; // convert degrees to radians for following calculations.
	b = b / 180. * M_PI;

	res = cnd_varpi (varpi, sigma_varpi, D) * int_d (D, l, b);

return res;
}
