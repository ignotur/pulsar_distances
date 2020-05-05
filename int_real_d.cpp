#include <cmath>
#include <iostream>
#include <cstdlib>

struct type_norm_factors {
double l;
double b;
double factor;
};


using namespace std;

extern "C" double int_d (double, double, double);

double int_d (double d, double l, double b) {
double res, h, H, z, R, step = 0.01, val;

double flag_is_computed;

static double l_test, b_test, norm_factor;
static int i_heap = 0;

static type_norm_factors norm_factors[100003];

h = 0.5;  // We are working with millisecond pulsars
H = 0.2 * 8.5; // 0.2
z = d * sin(b);
R = sqrt(8.5*8.5 + pow(d * cos(b), 2.0) - 2.0 * d * cos(b) * 8.5 * cos(l));
res = pow(d, 2.0) * pow(R, 1.9) * exp(-abs(z) / h - R / H);

flag_is_computed = false;
int i_found;

for (int i = 0; i < i_heap; i++)
	if (norm_factors[i].l == l and norm_factors[i].b == b) {
		i_found = i;
		flag_is_computed = true;
		break;
	}


//if (l_test != l || b_test != b) {
if (!flag_is_computed) {	
	//cout << "We have a new pulsar, let us search for a new normalisation factor. i_heap is "<< i_heap <<endl;
	norm_factor = 0.0;
	for (int i =0; i < 10000; i++) {
		d = i * step;
		z = d * sin(b);
		R = sqrt(8.5*8.5 + pow(d * cos(b), 2.0) - 2.0 * d * cos(b) * 8.5 * cos(l));
		val = pow(d, 2.0) * pow(R, 1.9) * exp(-abs(z) / h - R / H);
		norm_factor += step * val;
	}
	l_test = l;
	b_test = b;
	norm_factors[i_heap].l = l;
	norm_factors[i_heap].b = b;
	norm_factors[i_heap].factor = norm_factor;
	i_heap++;
	
	//cout << "Normalisation factor is "<<norm_factor<<endl;
}
else {
norm_factor = norm_factors[i_found].factor;
}

res = res / norm_factor;

//cout << "Check! If l and b are in radians!" << endl;

if (l > 2.1 * M_PI || b > M_PI) {
	cout << "l and b provided are not in radians!" <<endl;
	exit(6);
}
	

return res;
}
