# Learning Machines

Workshop series on data analysis and machine learning for astrophysics

# Table of Contents

## 0 - Python for data analysis 101

- Object Oriented Programming: take the green path and create a software ecosystem
- Numpy: killing the for-loop
- Scipy
- Matplotlib / k3d
- Astropy

## 1 - Optimization and Modeling

- Classical modeling: least-square basics (best fit and classic uncertainty estimation)
- LSMC: exploring the parameter space with Monte-Carlo
- code parallelization (writing multiple papers at the same time)
- Bayesian optimization and the Markov-Chain (chaining drunks)
- First steps on the Bayesian side of the force : Okham's razor, systematic errors and the power of priors.
 
- examples: 
  - Non-linear model fitting
  - M1, how to deconvolve multiple emission lines along the line-of-sight ?
  - Recover orbital parameters from a luminosity curve
 
## 2 - Old-School Machine Learning

- Detect patterns with convolution
- Pump up your Python (with Cython)
- Classification and modeling
  - PCA: how to start drawing curved lines
  - Walk through random forests and let the machines show you what you fail to see

- examples:
  - Find a thousand planetary nebulae in a 3 billion voxels haystack
  - Redefine the regions of the BPT diagram
 
 ## 3 - Deep learning
 
Make intelligence emerge from sand and practice ethical slavery

# Installation

installation instructions with Anaconda (should work on Linux, Mac OSX, Windows)

## 1. download Miniconda for your OS and python 3.7.

**If you already have [Anaconda](https://www.anaconda.com/) installed go to step 2**

instructions are here: [Miniconda — Conda](https://conda.io/miniconda.html)
1. place the downloaded file on your home directory
2. install it (use the real file name instead of `Miniconda*.sh`)
```bash
bash Miniconda*.sh
```
## 2. install `conda-build` tools
```bash
conda install conda-build
```

## 3. create your environment

create an environment and install needed modules manually
```bash
conda create -n learn python=3 .7 
conda install -n learn numpy scipy bottleneck matplotlib astropy cython h5py pandas
conda install -n learn -c conda-forge pyregion
conda install -n learn -c astropy photutils astroquery
```
if your shell is bash, which is now generally the case for OSX and most linux distributions please do
```
conda init bash
```
If you have a different shell replace bash with the name of your shell.

Now if you have Scisoft installed (which does not goes well with Anaconda/Python... but still you may want to have it)
then please add `export PYTHONPATH=''` at the end of your profile file where some environment variables are defined (e.g. `.bashrc`, `.profile`, `.bash_profile`).

You may then activate your environment with
```
conda activate learn
```
now your prompt should be something like `(learn) $`. If `conda activate learn` does not work. Please do the following `conda init bash` (if bash is your shell

note: you may now have to install `gcc` on Mac OSX or linux if you want to be able to execute the following with no error (see https://discussions.apple.com/thread/8336714). To check that you have gcc installed type `gcc --help` in a terminal. You should see the usage informations displayed.

e.g. to install `gcc` under ubuntu (or debian based distributions):

```bash
sudo apt update
sudo apt install build-essential
```

Then you can install the last python modules with pip (because those modules are not available via anaconda)
```bash
pip install gvar --no-deps
pip install lsqfit --no-deps
```


## 4. Install jupyter

```bash
conda install -n learn -c conda-forge jupyterlab
```
Run it

```bash
conda activate learn # you don't need to do it if you are already in the orb environment
jupyter lab
```
You should now have your web browser opened and showing the jupyter lab interface !



 
 
