# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:54:49 2018

@author: Qiao Yu
"""

def f(x):
    return 3
a = f(x)
    
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
        
        
stuff = ["iQ"]     
for thing in stuff:
        if thing == 'iQ':
           print("Found it")
           
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


## p3:
def closest_power(base, num):

    if num > 1:
        for i in range(0, int(num)):
            if base ** i < num and base **(i+1)>num:
                if abs(base ** i - num) <= abs(base**(i+1) - num):
                    return i
                else:
                    return i+1
            
    else:
        return 0
    
## p4:
def dotProduct(listA, listB):
    res = 0
    for i in range(len(listA)):
        res += listA[i]*listB[i]
    return res

## P5:


def uniqueValues(aDict):
    from collections import Counter
    m = [ ]
    n = [ ]
    l = Counter(aDict.values()).most_common()
    print(l)
    for x in l:
        if x[1] == 1:
            m.append(x[0])
    print(m)
    for x in m:
        n.append({v:k for k, v in aDict.items()}[x])
        
    return(sorted(n))
    
## P6:
def gcd(a, b):
    while b != 0:
        (a,b) = (b, a%b)
    return a

## P7:

def score(word, f):
    import string
    l = list((word).lower())
    s = []
    newlist = list(string.ascii_lowercase)
    a = dict(zip(newlist, list(range(1,27))))
    for i in range(len(l)):
        
        s.append(a[l[i]]*i)
    
    b = sorted(s)[-1]
    c = sorted(s)[-2]
    
    return(f(b,c))
    
    
    
    
    
            
        
    
             
    
    
        




































