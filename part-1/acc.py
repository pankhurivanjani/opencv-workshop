import random
import numpy as np
import scipy.io as sci

#loadmat loads .mat files. predictions.mat contains predictions made from classifier 
#and true_values.mat contains actual truth values.

true_values = sci.loadmat('true_values.mat')
predictions = sci.loadmat('predictions.mat')



#your task is to find accuracy percentage of this classifier
#based on the number of correct predictions made.
