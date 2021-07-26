
import re
def abbreviate(words):
    word = re.findall(r"[A-Za-z']+", words.upper())
    return "".join(i[0] for i in word)
