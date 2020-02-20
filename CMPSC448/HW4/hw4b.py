"""
CMPSC448 Machine Learning and AI Homework 4b
Calculus and Optimization from Scratch
Author: Joseph Sepich (jps6444)
"""

def question1_loss(w,X,y,indices,lamb,huber):
    """Calculates minibatch loss for huber loss of linear
    regression: sum(huber(y-yhat)) + lambda||w||^2
    
    Arguments:
        w {list} -- weights for linear regression model
        X {list[list]} -- Matrix of data features
        y {list} -- vector of true values
        indices {list} -- minibatch element indices
        lamb {numeric} -- regularization constant
        huber {function} -- huber loss function
    
    Returns:
        numeric -- minibatch loss
    """
    # minibatch loss is the sum of contributions of each point
    # to the objective function
    huber_loss = 0
    for i in indices:
        # calculate prediction
        # y_hat[i] = w * X[i] (dot product)
        y_hat = dot_product(w, X[i])
        # huber loss
        huber_loss += huber(y[i] - y_hat)
    # lamb * m / n * ||w||^2
    reg_contribution = (lamb * len(indices) / len(X)) * sum([w_elem**2 for w_elem in w])

    return huber_loss + reg_contribution

def question2_grad(w,X,y,indices,lamb,huber):
    """Calculates the minibatch gradient for huber loss
    of linear regression: sum(huber(y-yhat)) + lambda||w||^2
    
    Arguments:
        w {list} -- weight vector
        X {list[list]} -- Data feature matrix
        y {list} -- vector of true values
        indices {list} -- indices of minibatch
        lamb {numeric} -- regulariation constant
        huber {function} -- huber loss function
    
    Returns:
        numeric -- minibatch gradient result
    """
    # minibatch gradient is the result of running the
    # minibatch vectors through the graident function
    # gradient of objective function sum(huber(y-(w*X[i]))) + lambda||w||^2
    # sum(d_huber(y - y_hat)*X[i]) + 2*lambda*sum(w)
    huber_grad = 0
    for i in indices:
        # calculate pred
        y_hat = dot_product(w, X[i])
        # huber derivative
        huber_input = (y[i] - y_hat)
        if huber_input > 1:
            huber_grad += (huber_input / abs(huber_input) * X[i])
        else:
            huber_grad += (huber_input * X[i])
    huber_grad += (2 * lamb * len(indices) / len(X) * sum([w_elem for w_elem in w]))
    return huber_grad
    
def question3_update(w,X,y,indices,lamb,eta,huber):
    pass
    
def question4_n_updates(w,X,y,lamb,eta,mbatch,n,huber,shuffle):
    pass
    
def question5_nepochs(w,X,y,lamb,eta,mbatch,nepochs,huber,shuffle):
    pass
    
def question6_sgd(w,X,y,lamb,eta,mbatch,nepochs,epsilon,shuffle):
    pass

def dot_product(u, v):
    """Calculates the dot product between u and v
    
    Arguments:
        u {list} -- numeric vector
        v {list} -- numeric vector
    
    Returns:
        numeric -- scalar dot product of u and v
    """
    if len(u) != len(v):
        return None
    return sum(i[0] * i[1] for i in zip(u, v))
