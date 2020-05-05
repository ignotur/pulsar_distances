#include <cmath>
#include <iostream>

using namespace std;

extern "C" double cnd_varpi (double, double, double);

double cnd_varpi (double varpi, double sigma, double D) {
double res;

res = exp ( -0.5 * pow(varpi - 1.0/D, 2.0) / pow(sigma, 2.0)) / (sqrt(2.0*M_PI) * sigma);

//cout << mu << "\t" << sigma_mu << "\t" << D << "\t" << v << endl;

return res;
}
