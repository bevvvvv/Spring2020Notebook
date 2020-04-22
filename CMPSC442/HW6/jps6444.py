############################################################
# CMPSC 442: Homework 6
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.



############################################################
# Section 1: Hidden Markov Models
############################################################

def load_corpus(path):
    """Loads corpus at the given path. Must have token=POS format.
    
    Arguments:
        path {string} -- path to corpus text file
    
    Returns:
        list(tuple(string, string)) -- list of corpus sentences
    """
    # init output list
    sentences = [] 

    # read file
    f = open(path, 'r')
    corpus_sentences = f.read().splitlines()
    # parse each line as a sentence
    for sentence in corpus_sentences:
        # init single sentence list
        parsed_sentence = []
        # pairs seperated by white space
        corpus_pairs = sentence.split(' ')
        for corpus_pair in corpus_pairs:
            # convert token=POS to tuple
            pair = corpus_pair.split('=')
            # add pair to output
            parsed_sentence.append(tuple(pair))
        # add sentence to output
        sentences.append(parsed_sentence)

    # close file an return list
    f.close()
    return sentences

class Tagger(object):

    def __init__(self, sentences):
        pass

    def most_probable_tags(self, tokens):
        pass

    def viterbi_tags(self, tokens):
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
