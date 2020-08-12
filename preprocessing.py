import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

from collections import Counter


import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

## Menghilangkan spasi yang berlebihan
def remove_spaces(text):
  text=text.split()
  return ' '.join(text)

def lower_case(text):
  return text.lower()

def remove_punctuation(text):
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  no_punct = ""
  for char in text:
    if char not in punctuations:
      no_punct = no_punct + char
    else:
      no_punct = no_punct + ' '
  return no_punct

def remove_stopword(text):
    stop_words = stopwords.words('indonesian')
    stopwords_dict = Counter(stop_words)
    text = ' '.join([word for word in text.split() if word not in stopwords_dict])
    return text

def spell_checker(text):
  return text

def convert_emojis(text):
    for emot in emoji.UNICODE_EMOJI:
        text = re.sub(r'('+emot+')', "_".join(emoji.UNICODE_EMOJI[emot].replace(",","").replace(":","").split()), text)
    return text

def stemming(text):
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  return stemmer.stem(text)

def remove_number(text):
  return re.sub(r"\d+", "", text)

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(text): 
    tknzr = TweetTokenizer()
    return tknzr.tokenize(text)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
    
def remove_bl_word(words):
  blacklist_word = ['yg', 'n', 'nya', 'gak', 'ga','gk','tdk', 'aja', 'tp', 'sy', 'ya', '1', '2']
  for word in words:
    if word in blacklist_word:
      index = words.index(word)
      del words[index]
  return words