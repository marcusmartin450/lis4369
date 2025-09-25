#!/usr/bin/env python3

import sys
import jupyterlab
import pandas

# NOTE: DIFFERENCES (HYPHEN VS UNDERSCORE)!
# conda install pandas-datareader vs import pandas_datareader
# Note: pep8 underlines. Here, incorrectly identifying import errors!
import pandas_datareader
import numpy
import matplotlib
import sklearn
import django
import tensorflow
import scipy
import keras
import seaborn
import cv2  # opencv-python
import nltk
import statsmodels

# print default conda environment
# import os
# print(os.environ["CONDA_DEFAULT_ENV"] + "\n")

########## Resources: Formatting strings ##########
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/string.html#formatstrings

# F-Strings:
# https://the-examples-book.com/programming-languages/python/printing-and-f-strings#f-strings
########## END Resources: Formatting strings ##########

# old school print using % (DON’T USE! DEPRECATED!):
# print("Python version: %s" % sys.version)

# new school:
print('Python version: {0}'.format(sys.version))

# or, using F-Strings…
print(f"Python version: {sys.version}")

# adding newlines
print('Python version: \n{0}'.format(sys.version), "\n")

# print all Python version info
# print('Python version info: \n{0}'.format(sys.version_info), "\n")

# jupyterlab
print('jupyterlab: {0}'.format(jupyterlab.__version__))

# pandas
print('pandas: {0}'.format(pandas.__version__))

# pandas-datareader
print('pandas_datareader: {0}'.format(pandas_datareader.__version__))

# numpy
print('numpy: {0}'.format(numpy.__version__))

# matplotlib
print('matplotlib: {0}'.format(matplotlib.__version__))

# scikit-learn
print('sklearn: {0}'.format(sklearn.__version__))

# django
print('django: {0}'.format(django.__version__))

# tensorflow
print('tensorflow: {0}'.format(tensorflow.__version__))

# scipy
print('scipy: {0}'.format(scipy.__version__))

# keras
print('keras: {0}'.format(keras.__version__))

# seaborn
print('seaborn: {0}'.format(seaborn.__version__))

# cv2 (opencv-python)
print('cv2 (opencv-python): {0}'.format(cv2.__version__))

# nltk
print('nltk: {0}'.format(nltk.__version__))

# statsmodels
print('statsmodels: {0}'.format(statsmodels.__version__))
