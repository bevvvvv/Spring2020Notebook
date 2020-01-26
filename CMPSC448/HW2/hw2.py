"""
CMPSC448 Machine Learning and AI Homework 2
Decision Theory
Author: Joseph Sepich (jps6444)
"""

def q1(p, treatB, notTreatA, notTreatB):
    """Uses decision theory to determine the cost of treating a healthy patient
    that makes the cost of treating and not treating the same.

    :param p: Probability that the current patient is type A (healthy)
    :param treatB: cost of treating a sick patient
    :param notTreatA: cost of not treating a healthy patient
    :param notTreatB: cost of not treating a sick patient

    Example: ``q1(0.8, 10, 2, 20)``

    :return alpha: cost of treating a healthy patient
    """
    # probabilities
    prob_a = p
    prob_b = 1 - p

    # cost of not treating
    # recall cost -> sum(cost(decision) * probability cost is incurred)
    not_treat_cost = notTreatA * prob_a + notTreatB * prob_b

    # treat_cost = alpha * prob_a + treatB * prob_b
    # replace treat_cost with not_treat_cost since we want decision
    # to be indifferent (equal values for either decision)
    alpha = (not_treat_cost - treatB * prob_b) / prob_a

    return alpha

def q2(p, testCost, treatHealthy, treatCDS, notTreatHealthy, notTreatCDS):
    """Uses decision theory to determine if a patient should either
    be treated, not be treated, or have additional tests done.

    :param p: classifier output, probability patient has CDS
    :param testCost: cost of ordering a test
    :param treatHealthy: cost of treating a healthy patient
    :param treatCDS: cost of treating a sick patient
    :param notTreatHealthy: cost of not treating a healthy patient
    :param notTreatCDS: cost of not treating a sick patient

    Example: ``q2(0.05, 10, 5, 1, 10, 50)``

    :return decision: an integer 1, 0, -1 that determines whether to
    treat, order tests, or not treat the patient
    """
    # probabilities
    prob_cds = p
    prob_healthy = (1 - p)

    # cost of treatment
    treat_cost = treatHealthy * prob_healthy + treatCDS * prob_cds
    # cost of not treating
    not_treat_cost = notTreatHealthy * prob_healthy + notTreatCDS * prob_cds

    # return the minimum cost (defaults to lowest index)
    choices = [treat_cost, testCost, not_treat_cost]
    choice = choices.index(min(choices))
    if choice == 0:
        return 1
    if choice == 1:
        return 0
    return -1
