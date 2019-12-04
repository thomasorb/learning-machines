# lib.py
import numpy as np

class MyClass(object):
    
    def __init__(self, data):
        self.data = data
        
    def mymethod(self):
        print('mymethod: ', self.data)

def myrootmethod():
    print('hello')
    
a = 25


def PSF(r, fwhm, beta):
    alpha = fwhm / (2. * np.sqrt(2.**(1. / beta) - 1.))
    return (1. + (r/alpha)**2.)**(-beta)

def star(n, flux, x, y, fwhm=3, beta=3.5):
    Y, X = np.mgrid[:n, :n]
    X = X.astype(float) - x
    Y = Y.astype(float) - y
    R = np.sqrt(X**2 + Y**2)
    S = PSF(R, fwhm, beta)
    total_flux = np.sum(S)
    S = S / total_flux * flux
    return S