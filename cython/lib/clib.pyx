cimport cython
import cython

cimport numpy as np
import numpy as np

from cpython cimport bool

## Import functions from math.h (faster than python math.py)
cdef extern from "math.h" nogil:
    double cos(double theta)
    double sin(double theta)
    double exp(double x)
    double sqrt(double x)
    double log(double x)
    double ceil(double x)
    double floor(double x)
    double M_PI
    double isnan(double x)

# define long double for numpy arrays
ctypedef long double float128_t


@cython.boundscheck(False)
@cython.wraparound(False)
def gaussian_array2d(double h, double a, double dx, double dy, double fwhm,
                     int nx, int ny):
    """Return the 2D profile of a gaussian

    :param h: Height
    :param a: Amplitude
    :param dx: X position
    :param dy: Y position
    :param fwhm: FWHM
    :param nx: X dimension of the output array
    :param ny: Y dimension of the output array
    """
    cdef np.ndarray[np.float64_t, ndim=2] arr = np.zeros(
        (nx, ny), dtype=np.float64)
    cdef double r = 0.
    cdef double w = fwhm / (2. * sqrt(2. * log(2.)))
    cdef int ii, ij

    with nogil:
        for ii in range(nx):
            for ij in range(ny):
                r = sqrt(((<double> ii) - dx)**2. + ((<double> ij) - dy)**2.)
                arr[ii,ij] = h + a * exp((-r**2.)/(2.*(w**2.)))

    return arr
