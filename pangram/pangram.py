def is_pangram(sentence):
    
    line = sentence.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in alpha:
        if i not in line:
            return False
    return True
    
