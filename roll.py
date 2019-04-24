import random

def d4(bonus = 0):
    return roll(1, 4) + bonus

def d6(bonus = 0):
    return roll(1, 6) + bonus

def d8(bonus = 0):
    return roll(1, 8) + bonus

def d10(bonus = 0):
    return roll(1, 10) + bonus

def d20(bonus = 0):
    return roll((1, 20)) + bonus

def d100(bonus = 0):
    return 10*d10() + d10() + bonus

def roll(range):
    '''roll((1, 20)) => 1d20'''
    return random.randint(range[0], range[1])