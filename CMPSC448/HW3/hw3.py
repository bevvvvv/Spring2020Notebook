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
    MODEL_BASELINE = 0.6

    accuracy = 0
    for i in range(MAX_ITERATIONS):
        # run a trial on each model
        model_results = [np.random.binomial(n=TEST_SIZE, p=MODEL_BASELINE) for model in range(num_models)]
        accuracy += max(model_results) / TEST_SIZE
    return accuracy / MAX_ITERATIONS



def question2(num_models):
    """Determines how well a 0.6 accurate model does against
    n-1 other models with 0.5 accuracy.

    :param num_models: number of models (including one of the 60% accuracy)

    :return (a, b, c): (prob of outperform, prob of tie, prob of underperform)
    """
    TEST_SIZE = 20
    MAX_ITERATIONS = 1000000
    MODEL_BASELINE = 0.5
    MODEL_TEST = 0.6
    THRESHOLD = 0.001

    count_win = 0
    count_tie = 0
    count_loss = 0
    for i in range(MAX_ITERATIONS):
        # run one 0.6 and n-1 0.5
        model_results = [np.random.binomial(n=TEST_SIZE, p=MODEL_BASELINE) / TEST_SIZE \
             for model in range(num_models-1)]
        optimal_baseline = max(model_results)
        test_result = np.random.binomial(n=TEST_SIZE, p=MODEL_TEST) / TEST_SIZE
        diff = test_result - optimal_baseline
        if abs(diff) <= THRESHOLD:
            count_tie += 1
        elif diff > 0:
            count_win += 1
        else:
            count_loss += 1
    return (count_win / MAX_ITERATIONS, count_tie / MAX_ITERATIONS, count_loss / MAX_ITERATIONS)
    
def question3(results):
    """Determines the likelihood of seeing the correlation
    between two columns in results (being the same)

    :param results: 2D numpy array where results[i,0] and results[j,1] have
    the value of either 0 or 1

    :return p-value: likelihood of the number of correct guesses
    """
    MAX_ITERATIONS = 100000

    test_stats = []
    result_stat = len([row for row in results if row[0] == row[1]])
    for i in range(MAX_ITERATIONS):
        # single sim is one permutation and calc test stat
        np.random.shuffle(results[:, 0]) # permute a single column should break corr
        test_stat = len([row for row in results if row[0] == row[1]]) 
        test_stats.append(test_stat)
    p_value = len([stat for stat in test_stats if stat >= result_stat])
    p_value = p_value / MAX_ITERATIONS
    return p_value
