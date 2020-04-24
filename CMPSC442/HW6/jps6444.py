############################################################
# CMPSC 442: Homework 6
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import collections
import math
import sys



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

    def __init__(self, sentences, smoothing = 1e-5):
        self.corpus = sentences # if small enough to pass we can store in memory

        # count values
        start_tag_counts = collections.defaultdict(int)
        transition_counts = collections.defaultdict(int)
        emission_counts = collections.defaultdict(int)
        self.e_tokens = collections.defaultdict(list)
        self.tag_counts = collections.defaultdict(int) # calculate p(t_i) use in p(t_j | t_i) = p(t_j ^ t_i) / P(t_i)
        for sentence in self.corpus:
            # count start tags
            # tag index 1
            # token index 0
            start = sentence[0]
            start_tag_counts[start[1]] += 1
            # first index skipped below
            self.tag_counts[start[1]] += 1
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
                self.tag_counts[sentence[i][1]] += 1
        
        # tag probs
        self.tag_prob = {}
        for tag in self.tag_counts:
            self.tag_prob[tag] = self.tag_counts[tag] / sum(self.tag_counts.values())

        # calculate pi(t_i) -> start state prob, sentence starts with POS i
        self.pi = {}
        for tag in start_tag_counts.keys():
            self.pi[tag] = math.log((start_tag_counts[tag] + smoothing) / (sum(start_tag_counts.values()) + smoothing))
        self.pi['UNK'] = math.log(smoothing / (sum(start_tag_counts.values()) + smoothing))

        # calculate a(t_i -> t_j) -> transition prob POS i then j P(j | i)
        self.a = {}
        for transition in transition_counts.keys():
            # t_i to t_j listed as tuple key (t_i, t_j)
            self.a[transition] = math.log((transition_counts[transition] + smoothing) / (self.tag_counts[transition[0]] + smoothing))
        self.a['UNK'] = math.log(smoothing / (self.tag_counts[transition[0]] + smoothing))

        # calculate b(t_i -> w_i) -> emission/obs prob P(token | POS)
        self.b = {}
        for emission in emission_counts.keys():
            self.b[(emission[1], emission[0])] = math.log((emission_counts[emission] + smoothing) / (self.tag_counts[emission[1]] + smoothing))
        self.b['UNK'] = math.log(smoothing / (self.tag_counts[emission[1]] + smoothing))


    # LaPlace smoothing (handle novel inputs)
    def get_prob(self, p_type, param):
        """Gets the probability for start, transition, or emission.

        Arguments:
        p_type {string} -- pi, a, or b depending on prob type
        param {} -- input to probability structure in constructor
    
        Returns:
            float -- log prob
        """
        if p_type == 'a':
            try:
                return self.a[param]
            except:
                return self.a['UNK']
        elif p_type == 'b':
            try:
                return self.b[param]
            except:
                return self.b['UNK']
        else:
            try:
                return self.pi[param]
            except:
                return self.pi['UNK']

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
            max_prob = sys.maxsize * -1
            max_tag = ''
            for tag in self.e_tokens[token]:
                if self.get_prob('b', (tag, token)) >= max_prob:
                    max_prob = self.get_prob('b', (tag, token))
                    max_tag = tag
            tags.append(max_tag)
        return tags


    def viterbi_tags(self, tokens):
        """Returns the most viterbi tag seqence for token sequence
    
        Arguments:
            tokens {list(string)} -- list of tokens
        
        Returns:
            list(string) -- list of pos tags
        """
        seq_len = len(tokens)
        tags = list(self.tag_counts.keys())
        # tag by len (time)
        viterbi = [[0 for j in  range(seq_len)] for i in range(len(tags))] # init trellis to track
        back= [[0 for j in  range(seq_len)] for i in range(len(tags))] # init backpoint matrix

        # start probs
        for i in range(len(tags)):
            emission = (tags[i], tokens[0])
            viterbi[i][0] = self.get_prob('pi', tags[i]) + self.get_prob('b', emission)
            back[i][0] = -1

        # go through sequence
        for t in range(1, seq_len):
            # find likelihood of each possible tag
            for j in range(0, len(tags)):
                # find max transition of previous nodes
                max_val = sys.maxsize * -1
                max_tag_ind = 0
                for i in range(0, len(tags)):
                    transition = (tags[i], tags[j])
                    delta = viterbi[i][t - 1]
                    if self.get_prob('a', transition) + delta >= max_val:
                        max_val = self.get_prob('a', transition) + delta
                        max_tag_ind = i
                # add new viterbi value
                emission = (tags[j], tokens[t])
                viterbi[j][t] = max_val + self.get_prob('b', emission)
                back[j][t] = max_tag_ind

        # trace back
        t = seq_len - 1
        # find best end value
        max_val = sys.maxsize * -1
        max_tag_ind = 0
        for i in range(len(tags)):
            if viterbi[i][seq_len-1] >= max_val:
                max_val = viterbi[i][seq_len-1]
                max_tag_ind = i
        tags_out = [tags[max_tag_ind]]
        while t > 0:
            max_tag_ind = back[max_tag_ind][t]
            tags_out.insert(0, tags[max_tag_ind])
            t -= 1
        return tags_out

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
I spent approximately six hours on this assignment.
"""

feedback_question_2 = """
I found the viterbi algorithm the most challenging, because I had
not yet included LaPlace smoothing in my probability data structures, so
it was difficult to debug errors.
"""

feedback_question_3 = """
I like the demonstration between the most probable tag for
an individual token compared to its most probable tag when in a sequence.
This helped to illustrate how the hidden markov model works.
"""
