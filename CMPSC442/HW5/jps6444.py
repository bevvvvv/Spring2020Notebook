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
    text = re.sub(' +', ' ', text)
    text = text.strip()
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
        pass

    def update(self, sentence):
        pass

    def prob(self, context, token):
        pass

    def random_token(self, context):
        pass

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
