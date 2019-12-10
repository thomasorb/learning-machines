# Machine Learning and Artifical Intelligence in Astronomy


- [Data science](https://en.wikipedia.org/wiki/Data_science)

## Data and knowledge

- [DIKW pyramid](https://en.wikipedia.org/wiki/DIKW_pyramid): criticized hierarchical conception which considers that information is based on data, knowlege on information and wisdom on knowledge. But we can argue that data, information and knowledge are essentially synonyms. 

In all cases there is some sort of dimensionality reduction in the process of data extraction (distillation). This reduction is in fact a process of modeling which then offers ways to generalize, extrapolate or predict new data.

- Model [https://en.wikipedia.org/wiki/Scientific_modelling]: A mathematical model is a function which reduces some data to a reduced number of parameters. A model reduces the dimensionality of a data vector.

Y ~ Ŷ = f(X, P)
- Y = data vector
- Ŷ = approx. to data vector
- f = model
- X = vector of free parameters
- P = vector of fixed internal parameters

X = f(P, Y)


For f to be a model, X must be smaller than Y.

Example 1: Let's say we have a 64x64 image. The dimensionality of an image is equal to the number of pixels (in machine-learning we use the term features), i.e. Y = 4096 pixels. A binary classificator which tells if it's a cat or not is a model which will reduce the data size to one boolean parameter (X = 1 boolean). The internal parameters of the model (e.g. the weights and structure of a neural network) may be arbitrary high.

Example 2: Calibrated data is also a model (based on a lot of physical and instrumental knowledge) which permit to reduce the data obtained on a target (e.g. an image) + some calibration data (at least, the observation date, the direction of the telescope, sometimes a set of calibration images) to a calibrated image. Y is the flux in an integrated bandpass. Ŷ is the raw image + the calibration data, P is the calibrated image and X can be the set of RA/DEC coordinates (containted in the FOV of the image) for which I can obtain the integrated flux (in a given bandpass). 

In general, f is an algorithm based on finite set of internal parameters P which must be fitted so that Y ~ f(X)

Machine-learning:

> Automated processes that learn by example in order to classify, predict, discover or generate new data [2]




- Data size is increasingly larger and becomes eventualy too large to be treated by hand (small DIY coding).
- Task is not trivial

- A number of powerful and well-implemented tools have been developed. It is better to know they exists before doing it yourself from scratch.


- We may know exactly what to do but we cannot do it by hand
- We do not know exactly how features correlate but we have the feeling that some function applied to the features may lead to



## Tasks

- Classification
- Regression
- Clustering
- Forecasting
- Generation and Reconstruction
- Discovery
- Insight

## Tools

- Principal Component Analysis (PCA)
- Random Forests (RF)
- Support Vector machines (SVMs)
- Artificial Neural Networks (ANN)




## Bibliography

- [1]: Željko, I., (2014) Statistics, Data Mining, and Machine Learning in Astronomy
- [2]: Fluke, J., Jacobs, C., (2019) Surveying the reach and maturity of machine learning and artificial intelligence in astronomy
