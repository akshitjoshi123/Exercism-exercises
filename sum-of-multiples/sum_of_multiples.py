def sum_of_multiples(limit, multiples):
    list1 = []    
    for n in range(1,limit):
        for m in multiples:
            val = n*m
            if val < limit and not val in list1:
                list1.append(val)
    return sum(list1)
