import random as rand

def check(range, threshold):
    r1 = rand.randint(range[0], range[1])
    if r1 > threshold:
        return True
    else:
        return False

