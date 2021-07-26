import re
from collections import Counter

def count_words(sentence):
    word = r"[a-z\d]+(?:'[a-z\d])?"
    low = sentence.lower()
    words = re.findall(word, low)
    return Counter(words)
