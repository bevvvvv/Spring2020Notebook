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
        list -- gradient vector w.r.t w
    """
    # minibatch gradient is the result of running the
    # minibatch vectors through the graident function
    # gradient of objective function sum(huber(y-(w*X[i]))) + lambda||w||^2
    # sum(d_huber(y - y_hat)*X[i]) + 2*lambda*sum(w)
    huber_grad = []
    for col in range(len(w)):
        # go down each column in X (matches to a weight)
        next_grad_val = 0
        for i in indices:
            # calculate pred
            y_hat = dot_product(w, X[i])
            # huber derivative
            huber_input = (y[i] - y_hat)
            if huber_input > 1:
                next_grad_val += (huber_input / abs(huber_input) * -1 * X[i][col])
            else:
                next_grad_val += (huber_input * -1 * X[i][col])
            next_grad_val += (2 * lamb * len(indices) / len(X) * w[col]) # gradient from regularization
        huber_grad.append(next_grad_val)
    return huber_grad
    
def question3_update(w,X,y,indices,lamb,eta,huber):
    """Computes updated weight parameters for our linear
    regression huber loss model.
    
    Arguments:
        w {list} -- weight vector
        X {list[list]} -- matrix of data features
        y {list} -- vector of true values
        indices {list} -- indicies of minibatch
        lamb {numeric} -- regularization coefficient
        eta {numeric} -- MBSGD learning rate
        huber {function} -- huber loss function
    
    Returns:
        list -- updated weight vector
    """
    updated_w = []
    grad = question2_grad(w, X, y, indices, lamb, huber)
    for col in range(len(w)):
        # each weight
        new_w = w[col] - (eta * grad[col])
        updated_w.append(new_w)
    return updated_w
    
def question4_n_updates(w,X,y,lamb,eta,mbatch,n,huber,shuffle):
    """Returns the value of the weight vector after n updates.
    
    Arguments:
        w {list} -- weight parameter vector
        X {list[list]} -- data feature matrix
        y {list} -- vector of true values
        lamb {numeric} -- value of regularization constant
        eta {numeric} -- gradient descent learning rate
        mbatch {numeric} -- size of minibatch
        n {numeric} -- number of updates to perform
        huber {function} -- huber loss function
        shuffle {function} -- shuffling function
    
    Returns:
        list -- update weight parameter vector
    """
    # Steps
    # shuffle data
    # get first m record indicies and use update function
    # continue to next
    X, y = shuffle(X, y) # shuffled dataset
    start_index = 0
    dataset_size = len(X)
    update_count = 0
    while start_index + mbatch <= dataset_size and update_count < n:
        indices = range(start_index, (start_index + mbatch))
        w = question3_update(w, X, y, indices, lamb, eta, huber)
        update_count += 1
        start_index += mbatch
    if start_index < (dataset_size - 1): # less than mbatch size
        indices = range(start_index, (dataset_size - start_index))
        w = question3_update(w, X, y, indices, lamb, eta, huber)
        update_count += 1
    if update_count < n: # start a new epoch
        w = question4_n_updates(w, X, y, lamb, eta, mbatch, (n - update_count), huber, shuffle)
    return w
    
def question5_nepochs(w,X,y,lamb,eta,mbatch,nepochs,huber,shuffle):
    for i in range(nepochs):
        steps = len(X) // mbatch
        if len(X) % mbatch != 0:
            steps += 1
        w = question4_n_updates(w, X, y, lamb, eta, mbatch, steps, huber, shuffle)
    return w
    
def question6_sgd(w,X,y,lamb,eta,mbatch,nepochs,epsilon,shuffle):
    def eploss(z):
        if abs(z) <= epsilon:
            return 0
        elif z > epsilon:
            return (z - epsilon)**2
        return (z + epsilon)**2
    for i in range(nepochs):
        steps = len(X) // mbatch
        if len(X) % mbatch != 0:
            steps += 1
        w = question6_n_updates(w,X,y,lamb,eta,mbatch,steps,eploss,epsilon,shuffle)
    return w

def question6_grad(w,X,y,indices,lamb,eploss, epsilon):
    """Calculates the minibatch gradient for epsilon insensitive loss
    of linear regression: sum(l(y-yhat)) + lambda||w||^2
    
    Arguments:
        w {list} -- weight vector
        X {list[list]} -- Data feature matrix
        y {list} -- vector of true values
        indices {list} -- indices of minibatch
        lamb {numeric} -- regulariation constant
        eploss {function} -- epsilon insensitive loss function
        epsilon {numeric} -- eploss epsilon constant
    
    Returns:
        list -- gradient vector w.r.t w
    """
    # minibatch gradient is the result of running the
    # minibatch vectors through the graident function
    # gradient of objective function sum(huber(y-(w*X[i]))) + lambda||w||^2
    # sum(d_huber(y - y_hat)*X[i]) + 2*lambda*sum(w)
    huber_grad = []
    for col in range(len(w)):
        # go down each column in X (matches to a weight)
        next_grad_val = 0
        for i in indices:
            # calculate pred
            y_hat = dot_product(w, X[i])
            # eploss derivative
            eploss_input = (y[i] - y_hat)
            if abs(eploss_input) <= epsilon:
                next_grad_val += 0
            elif eploss_input > epsilon:
                next_grad_val += (2 * (eploss_input - epsilon) * -1 * X[i][col])
            elif eploss_input < -epsilon:
                next_grad_val += (2 * (eploss_input + epsilon) * -1 * X[i][col])
            next_grad_val += (2 * lamb * len(indices) / len(X) * w[col]) # gradient from regularization
        huber_grad.append(next_grad_val)
    return huber_grad
    
def question6_update(w,X,y,indices,lamb,eta,eploss, epsilon):
    """Computes updated weight parameters for our linear
    regression epsilon insensitive loss model.
    
    Arguments:
        w {list} -- weight vector
        X {list[list]} -- matrix of data features
        y {list} -- vector of true values
        indices {list} -- indicies of minibatch
        lamb {numeric} -- regularization coefficient
        eta {numeric} -- MBSGD learning rate
        eploss {function} -- epsilon insensitive loss function
        epsilon {numeric} -- eploss epsilon constant
    
    Returns:
        list -- updated weight vector
    """
    updated_w = []
    grad = question6_grad(w, X, y, indices, lamb, eploss, epsilon)
    for col in range(len(w)):
        # each weight
        new_w = w[col] - (eta * grad[col])
        updated_w.append(new_w)
    return updated_w
    
def question6_n_updates(w,X,y,lamb,eta,mbatch,n,eploss,epsilon,shuffle):
    """Returns the value of the weight vector after n updates.
    
    Arguments:
        w {list} -- weight parameter vector
        X {list[list]} -- data feature matrix
        y {list} -- vector of true values
        lamb {numeric} -- value of regularization constant
        eta {numeric} -- gradient descent learning rate
        mbatch {numeric} -- size of minibatch
        n {numeric} -- number of updates to perform
        eploss {function} -- epsilon insensitive loss function
        epsilon {numeric} -- eploss epsilon constant
        shuffle {function} -- shuffling function
    
    Returns:
        list -- update weight parameter vector
    """
    # Steps
    # shuffle data
    # get first m record indicies and use update function
    # continue to next
    X, y = shuffle(X, y) # shuffled dataset
    start_index = 0
    dataset_size = len(X)
    update_count = 0
    while start_index + mbatch <= dataset_size and update_count < n:
        indices = range(start_index, (start_index + mbatch))
        w = question6_update(w, X, y, indices, lamb, eta, eploss, epsilon)
        update_count += 1
        start_index += mbatch
    if start_index < (dataset_size - 1): # less than mbatch size
        indices = range(start_index, (dataset_size - start_index))
        w = question6_update(w, X, y, indices, lamb, eta, eploss, epsilon)
        update_count += 1
    if update_count < n:
        w = question6_n_updates(w, X, y, lamb, eta, mbatch, (n - update_count), eploss, epsilon, shuffle)
    return w

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
