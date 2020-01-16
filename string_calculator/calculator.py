import re

def add(string):
    sum = 0

    if len(string) == 0: 
        return 0
    
    if len(string) == 1:
        return int(string)
    
    elif string[0] == "/":
        result = 0 
        delim = string[3]

    else:
        result = 0
        delim = ","
        if string[1]!=",":
            delim = "\n"
            numbers = string.split(delim)

    numbers = re.findall(r"\d+|-\d+",string)
    negetive_numbers = []
    positive_numbers = []
    total = 0

    for i, num in enumerate(numbers):
        if int(num) < 0:
            negetive_numbers.append(int(num))
    
        if int(num) > 0:
            positive_numbers.append(int(num))

            # if int(num) >= 1000:
    for i, x in enumerate(positive_numbers):
        if int(x) >1000:
            positive_numbers[i] = 0

    if len(negetive_numbers) > 0:
        raise Exception('negatives not allowed: {}'.format(negetive_numbers))
    else:
        for i in positive_numbers:
            total += int(i)
    return total
    


    