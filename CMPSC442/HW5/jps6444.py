############################################################
# CMPSC 442: Homework 5
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string
import re
import collections
import random
import math


############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    """Extracts token from input string.
    A token is any contiguous sequence of non-whitespace
    characters, with the exception that any punctuation mark
    be considered its own token.
    
    Arguments:
        text {string} -- string to tokenize
    
    Returns:
        list[string] -- list of tokens
    """
    text = text.strip() + ' '
    text = re.sub(' +', ' ', text)
    tokens = []
    start = 0
    end = 0
    while end < len(text):
        if text[start] == ' ':
            start += 1
            end = start
            continue
        if text[end] == ' ' and abs(end - start) > 0: # end of non-white
            tokens.append(text[start:end])
            start = end + 1
        elif text[end] in string.punctuation:
            if abs(end - start) > 0:
                tokens.append(text[start:end])
            tokens.append(text[end:end + 1])
            start = end + 1
        end += 1
    return tokens

def ngrams(n, tokens):
    """Given a list of tokens, returns a list of n-grams.
    
    Arguments:
        n {integer} -- size of token plus context
        tokens {list[string]} -- list of tokens
    
    Returns:
        list[tuple(tuple(), string)] -- list of tokens with context
    """
    # add padding
    for i in range(n-1):
        tokens.insert(0, '<START>')
    tokens.append('<END>')
    grams = []
    for i in range(n-1,len(tokens)):
        grams.append((tuple(tokens[i-n+1:i]), tokens[i]))
    return grams

class NgramModel(object):

    def __init__(self, n):
        self.order = n
        self.contexts = collections.defaultdict(int) # count of contexts
        self.seqs = collections.defaultdict(int) # count of token and context
        self.tokens = collections.defaultdict(list) # tokens associated with context

    def update(self, sentence):
        """Updates counts of sequences.
        
        Arguments:
            sentence {string} -- string to add to language model
        """
        new_grams = ngrams(self.order, tokenize(sentence))
        for gram in new_grams:
            self.contexts[gram[0]] += 1
            if gram[1] not in self.tokens[gram[0]]: # track tokens of context
                self.tokens[gram[0]].append(gram[1])
            self.seqs[gram] += 1


    def prob(self, context, token):
        """Calculates probability of token given context.
        
        Arguments:
            context {tuple(string)} -- tuple of strings length n
            token {string} -- word of interest
        
        Returns:
            double -- probaility of token given context
        """
        return self.seqs[(context, token)] / self.contexts[context]

    def random_token(self, context):
        """Returns a random token associated with the given context.
        
        Arguments:
            context {tuple(string)} -- sequence of tokens
        
        Returns:
            string -- a token associated with the given context
        """
        r = random.random()
        probs = [(self.prob(context, token), token) for token in self.tokens[context]]
        probs.sort(key = lambda tup: tup[1]) # sort by token
        prob_sum = 0
        for prob in probs:
            prob_sum += prob[0]
            if prob_sum <= r:
                continue
            else:
                return prob[1]

    def random_text(self, token_count):
        """Creates random sentence from ngram model.
        
        Arguments:
            token_count {int} -- number of tokens in sentence
        
        Returns:
            string -- new sentence
        """
        start_context = ['<START>' for i in range(self.order - 1)]
        context = start_context[:]
        count = 0
        output = ''
        while count < token_count:
            new_token = self.random_token(tuple(context))
            output += new_token + ' '
            count += 1
            # update context
            if new_token == '<END>' or self.order == 1:
                context = start_context[:]
            else:
                context.pop(0)
                context.append(new_token)
        return output.strip()

    def perplexity(self, sentence):
        """Calculates the perplexity of the given sentence according
        to the NgramModel
        
        Arguments:
            sentence {string} -- sentence of tokens
        
        Returns:
            double -- perplexity value of sentence
        """
        grams = ngrams(self.order, tokenize(sentence))
        inner = 0
        exponent = 0
        for gram in grams:
            prob = self.prob(gram[0], gram[1])
            inner += math.log(1 / prob)
            exponent += 1 # count number of terms
        return math.exp(inner) ** (1 / exponent)

def create_ngram_model(n, path):
    """Creates an ngram model from the text in the given file.
    
    Arguments:
        n {int} -- order of the ngram model
        path {string} -- path to text file
    
    Returns:
        NgramModel -- NgramModel of given text data
    """
    model = NgramModel(n)
    with open(path, 'r') as text:
        lines = text.readlines()
        for line in lines:
            model.update(line)
    return model

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
I spent approximately ten hours on this assignment.
"""

feedback_question_2 = """
I found the random token method the most challenging. At first I did not
understand the formula, because I didn't realize that the probabilities
had to sum to one. I also found perplexity difficult due to the high degree
of precision.
"""

feedback_question_3 = """
I liked how this assignment was broke down into appropriate sized functions
for creating this first order Markov Model. It seems like this homework will
be invaluable for creating the HMM in the next asssignment.
"""
