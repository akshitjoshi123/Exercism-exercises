def is_isogram(string):
    string_lower = string.lower()

    string_list = []

    for i in string_lower:
        if i.isalpha():
            if i in string_list:
                return False
            string_list.append(i)
    return True
