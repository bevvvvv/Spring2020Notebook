############################################################
# CMPSC 442: Homework 6
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import collections



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
        self.corpus = sentences # if small enough to pass we can store in memory

        # count values
        start_tag_counts = collections.defaultdict(int)
        transition_counts = collections.defaultdict(int)
        emission_counts = collections.defaultdict(int)
        self.e_tokens = collections.defaultdict(list)
        tag_counts = collections.defaultdict(int) # calculate p(t_i) use in p(t_j | t_i) = p(t_j ^ t_i) / P(t_i)
        for sentence in self.corpus:
            # count start tags
            # tag index 1
            # token index 0
            start = sentence[0]
            start_tag_counts[start[1]] += 1
            # first index skipped below
            tag_counts[start[1]] += 1
            emission_counts[start] += 1 # tuple key!

            for i in range(1, len(sentence)):
                # count transmissions
                transition_counts[(sentence[i-1][1], sentence[i][1])] += 1

                # count emission
                emission_counts[sentence[i]] += 1
                # track token POS for most_prob_tags
                if sentence[i][1] not in  self.e_tokens[sentence[i][0]]:
                    self.e_tokens[sentence[i][0]].append(sentence[i][1])

                # count tags
                tag_counts[sentence[i][1]] += 1
        
        # tag probs
        self.tag_prob = {}
        for tag in tag_counts:
            self.tag_prob[tag] = tag_counts[tag] / sum(tag_counts.values())

        # calculate pi(t_i) -> start state prob, sentence starts with POS i
        self.pi = {}
        for tag in start_tag_counts.keys():
            self.pi[tag] = start_tag_counts[tag] / sum(start_tag_counts.values())

        # calculate a(t_i -> t_j) -> transition prob POS i then j P(j | i)
        self.a = {}
        for transition in transition_counts.keys():
            # t_i to t_j listed as tuple key (t_i, t_j)
            self.a[transition] = transition_counts[transition] / tag_counts[transition[0]]

        # calculate b(t_i -> w_i) -> emission/obs prob P(token | POS)
        self.b = {}
        for emission in emission_counts.keys():
            self.b[(emission[1], emission[0])] = emission_counts[emission] / tag_counts[emission[1]]

        # LaPlace smoothing (handle novel inputs)

    def most_probable_tags(self, tokens):
        """Returns the most probable tag for each token requested
    
        Arguments:
            tokens {list(string)} -- list of tokens
        
        Returns:
            list(string) -- list of matching pos tags
        """
        tags = []
        for token in tokens:
            # get all emission probs
            max_prob = 0
            max_tag = ''
            for tag in self.e_tokens[token]:
                if self.b[(tag, token)] >= max_prob:
                    max_prob = self.b[(tag, token)]
                    max_tag = tag
            tags.append(max_tag)
        return tags


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
