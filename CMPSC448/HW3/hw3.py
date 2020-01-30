"""
CMPSC448 Machine Learning and AI Homework 3
Randomization
Author: Joseph Sepich (jps6444)
"""
import numpy as np

def question1(num_models):
    """States best performing model of n models with baseline of p=0.6
    on a validation set of size n=10

    :param num_models: The number of models (integer)

    :return accuracy: accuracy of empirically best performing model
    """
    TEST_SIZE = 10
    MAX_ITERATIONS = 10000

    accuracy = 0
    for i in range(MAX_ITERATIONS):
        # run a trial on each model
        model_results = [np.random.binomial(n=TEST_SIZE, p=0.6) for model in range(num_models)]
        accuracy += max(model_results) / TEST_SIZE
    return accuracy / MAX_ITERATIONS



def question2(num_models):
    pass
    
def question3(results):
    pass
