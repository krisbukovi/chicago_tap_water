# filename: tf_nn.py
# author: kris bukovi
# last modified: July 21, 2018

import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops

def load_dataset():

def random_mini_batches(X, Y, mini_batch_size = 64, seed = 0):

def convert_to_one_hot(Y, C):

def predict(X, parameters):

def forward_propagation_for_predict(X, parameters):

def one_hot_matrix(labels, C):

def ones(shape):

def create_placeholders(n_x, n_y):

def initialize_parameters():

def forward_propagation(X, parameters):

def compute_cost(Z3, Y):

def model(X_train, Y_train, X_test, Y_test, learning_rate = 0.0001,
            num_epochs = 1500, minibatch_size = 32, print_cost = True):

