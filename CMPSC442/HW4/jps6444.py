############################################################
# CMPSC442: Homework 4
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import email

############################################################
# Section 1: Spam Filter
############################################################

def load_tokens(email_path):
    """Loads all text tokens from email at file path
    into a list.
    
    Arguments:
        email_path {string} -- path to email file on disk
    
    Returns:
        list[string] -- list of text tokens
    """
    # read message from file
    message = email.message_from_file(email_path)
    # create list of tokens
    tokens = []
    for line in email.iterators.body_line_iterator(message):
        [tokens.append(token) for token in line.strip().split(' ')]
    return tokens

def log_probs(email_paths, smoothing):
    pass

class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):
        pass
    
    def is_spam(self, email_path):
        pass

    def most_indicative_spam(self, n):
        pass

    def most_indicative_ham(self, n):
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
