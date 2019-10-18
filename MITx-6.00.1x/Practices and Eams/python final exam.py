# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:56:53 2018

@author: Qiao Yu
"""
# 3. 
'''
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
'''
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    
    a = int(us_num) // 10
    b = int(us_num) % 10
    if us_num == '10':
        return trans['10']
    while us_num != '10':
        if a == 0:
            return trans[str(b)]
        elif a != 0: 
            if b == 0:
                return trans[str(a)] + " " + trans['10']
            elif a == 1:
                return trans['10']  + " " + trans[str(b)] 
            else:
                return trans[str(a)] + " " + trans['10'] + " " + trans[str(b)]
            
# 4.

from collections import Counter

def is_list_permutation(L1, L2):
    c = Counter(L1)
    if c != Counter(L2):
        return False
    if not c:
        return (None, None, None)
    value, count = c.most_common(1)[0]
    return value, count, type(value)

# 5.
def cipher(map_from, map_to, code):
    myDict = {}
    for i in range(len(map_from)):
        name = map_from[i]
        value = map_to[i]
        myDict[name] = value
    
    
    code = list(code)
    res = []
    for i in range(len(code)):
        temp = myDict[code[i]]
        res.append(temp)
    res = ''.join(res)
    return (myDict, res)

# 7.
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        if e in self.vals.keys():
            self.vals[e] -= 1
        else:
            return 0

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals.keys():
            return self.vals[e]
        else:
            return 0
        
    
d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)


d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
print(d1.count(2))
print(d1.count(4))
    
    
    

































