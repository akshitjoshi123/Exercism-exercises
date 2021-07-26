def is_armstrong_number(number):

    n1 = len(str(number))
    sum = 0
    
    for i in str(number):
        sum += int(i) ** n1
    return number == sum