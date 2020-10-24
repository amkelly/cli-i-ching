# python implimentation of various i-ching divination methods

from random import randrange

def threecoin():
    hexagram = []
    l = 0
    while l < 6:
        toss, t = [], 0
        while t < 3:
            t += 1
            toss.append(randrange(2,4)) #value between 2 and 3, coin flip
        #print(toss)
        if sum(toss) == 6:
            print('---x---  6 [old yin]')
        elif sum(toss) == 7:
            print('--- ---  7 [young yin]')
        elif sum(toss) == 8:
            print('---o---  8 [young yang]')
        else:
            print('-------  9[old yang]')
        l += 1
            
def mod_threecoin():
    '''not implimented'''

def yarrowstalks():
    '''not implimented'''

hexagram_lookup = {
    1: 111111,
    2: 000000,
    3: 'x'}
    
h01 = {
    "number": 1,
    "name_en": 'Force',
    "name_ch": 'quian',
    "unicode": '\u4DC0' # can replace with chr(1234) function to turn into to unicode char.
    }

h02 = {
    "number": 2,
    "unicode": '\u4DC1'
    }

h03 = {
    "number": 3}

threecoin()
    
