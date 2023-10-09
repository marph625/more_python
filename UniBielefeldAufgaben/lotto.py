import random

def Lotto(x):
    # initialize empty list
    list = []

    # instead of a for loop use a while loop and use the len() function
    # while the amount of the elements of the list is less than x, do...
    while len(list) < x:
        randnum = random.randint(1, 49)
        if randnum not in list:
            list.append(randnum)
    print(sorted(list))

Lotto(6)