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
        pass

    def perplexity(self, sentence):
        pass

def create_ngram_model(n, path):
    pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
