# Pulsar Distances

Simple code to estimate the posterior distance distribution given the measured parallax. The parameters of the prior are adapted for millisecond radio pulsars.

The equations are presented in Igoshev, Verbunt & Cator (2016). 

## How to compile

In order to compile the code it is necessary to type 

```
make
```

This action prepares a library d_post.so which contains functions to compute the conditional probability, prior and posterior for distances.
This library could be added to another project in C++ or linked to e.g. Python code. Here I provide two python example of the code usage based on
parameters of PSR J0218+4232. 

## Examples of usage

### Simple posterior

The example can be found in plot_posterior.py. This script contains following lines with pulsar parameters:

```
## Example for PSR J0218+4232

gl = 139.51
gb = -17.53
varpi     = 0.16    ## mas
varpi_err = 0.09
```

Here gl and gb are the Galactic longuitude and latitude (requred by prior), varpi and varpi_err are the measured parallax and parallax error. 
Code produces the following figure.

![Posterior distance distribution for PSR J0218+4232](https://github.com/ignotur/pulsar_distances/blob/master/posterior.png)

### Contribution of measurement and prior

The code plot_illustration.py shows individual contribution of the measurement and the prior. For example, in the case of the pulsar J0218+4232, the measurement formally allows the infinite distance. On the other hand, the prior assumes that the pulsar belongs to the Galactic disk population, so large distances are exponentially suppressed.
The example is shown in the following figure.

![Posterior distance distribution for PSR J0218+4232 together with prior and measurement](https://github.com/ignotur/pulsar_distances/blob/master/illustration.png)


### File content

File `cnd_varpi.cpp` contains the description of the conditional probability g( varpi | D ).

File `int_real_d.cpp` contains the Galactic distance prior f_D (D).

File `posterior.cpp` combines prior and conditional probability and computes posterior for any distance restricted by 100 kpc (prior is normalised only up until this distance).

## Troubleshooting 

If code is compiled using a linux machine, a line in the makefile should be replaced with:

```
g++ -fPIC -shared -O3 cnd_varpi.cpp int_real_d.cpp posterior.cpp -o d_post.so 
```


