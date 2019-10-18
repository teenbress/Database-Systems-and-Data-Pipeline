# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:11:33 2018

@author: Qiao Yu
"""
# lecture 3#
# square root of int;
ans = 0
neg_flag = False
x = int(input('Enter an integer: '))
if x < 0:
    neg_flag = True
while ans ** 2 < x:
    ans = ans + 1
if ans ** 2 == x:
    print ("Square root of ", x, "is ", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")
        
## cheer world';
an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a world: ")
times = int(input("Enthusiasm level(1-10): "))

i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an "+ char +"! "+char)
    else:
        print("Give me a "+ char + "!" + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word,"!!!")

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
        
        
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1   
    
    
## bisection applied on the square root;
x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high+low)/2

while abs(ans**2-x) >= epsilon:
    print('low = '+str(low)+' high = '+str(high) + ' ans = '+str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = '+ str(numGuesses))
print(str(ans)+' is close to square root of '+str(x))

##guess the figure;

#print("Please think of a number between 0 and 100!")
#x = 100
#low = 0
#high = x
#guess = int((high+low)/2)
#while guess <= x:
#    guess = int((high+low)/2)
#    print('Is your secret number ' + str(guess)+'?')
#    ans= input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
#    if ans == 'c':
#        print ('Game over. Your secret number was: '+ str(guess))
#        break
#    else:
#        if ans == 'l':
#            low = guess
#        elif ans == 'h':
#            high = guess
#        else:
#            print ('Sorry, I did not understand your input.')
#    

def g(x):
    def h():
        x = 'abc'
    x = x+1
    print('in g(x): x =',x)
    h()
    return x
x = 3
z = g(x)
    
def a(x, y, z):
    if x:
        return y
    else:
        return z
    
  a = 10
def f(x):
    return x+a
a=3
f(1)

def foo (x):
    def bar(z,x=0):
        return z+x
    return bar(3)
foo(5)

str1 = 'exterminate!'
str2 = 'number one - the larch'
str2 = 'number one - the larch'
str2.index('n')

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
 return x % 2 == 1

def iterPower(base,exp):
    result = 1
    while exp >0:
        result *= base
        exp -=1
    return result

def recurPower(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base* recurPower(base,exp-1)

## the greatest common divisor;

#def gcdIter(a, b):
#    re = min (a, b)
#    while a % re != 0 or b % re != 0:
#        re -= 1
#    return re

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
def isIn(char, aStr):
    ## if aStr is empty:
    if aStr == '':
        return False
    ## if aStr is single character:
    if len(aStr) == 1:
        return char == aStr
    ## if aStr is a normal string:
    if len(aStr) > 1:
        midIndex = len(aStr)//2
        if char == aStr[midIndex]:
            return True
        elif char < aStr[midIndex]:
            return isIn(char, aStr[:midIndex])
        else:
            return isIn(char, aStr[midIndex+1:])

def polysum(n,s):
    import math
    def area(n,s):
        return 0.25 * n * s**2 /math.tan(math.pi/n)
    def peri(n,s):
       return n * s
    return round(area(n,s)+peri(n,s)**2, 4)


## case problem set 2;

#def remainBalance(b, r, m):
#    """
#    b is balance;
#    r is annual interest rate;
#    m is monthly payment rate;
#    n is the number of month,here n = 12;
#    """

#    def remainBalance(b,r,m,n):
#        return round((1-m)**n * b * (1+r/12.0)**n, 2)
#    remainB =  round((1-m)**12 * b * (1+r/12)**12, 2)
#    print ("Remaining balance: ", remainB)
#  
#def remainBalance(balance, annualInterestRate, monthlyPaymentRate):
#    remainB =  round((1-monthlyPaymentRate)**12 * balance * (1+annualInterestRate/12)**12, 2)
#    return remainB
#    print ("Remaining balance: ", remainB)   
#
#
#def remainBalance(balance, annualInterestRate, monthlyPaymentRate):
#    remainB =  round((1-monthlyPaymentRate)**12 * balance * (1+annualInterestRate/12)**12, 2)
#    return print ("Remaining balance: ", remainB)  
#
#def minPayment(balance, annualInterestRate, monthlyPaymentRate):
#    remainB =  round((1-monthlyPaymentRate)**12 * balance * (1+annualInterestRate/12)**12, 2)
#    return print ("Remaining balance: ", remainB) 

## credit card: without def a function:
month = 1
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
while month < 13:
    balance *= (1-monthlyPaymentRate)*(1+annualInterestRate/12) 
    month += 1
print("Remaining balance: ", round(balance,2))

## paying debt off in a year;
balance = 3926
annualInterestRate = 0.2
payment = 10
add=10
month = 0
unBalance = balance 
while month < 13:
    unBalance -= payment
    unBalance *= (1+ annualInterestRate/12)
    month += 1
    if month == 12:
        if unBalance > 0:
            payment += add
            month = 0
            unBalance = balance
        else:
            print(unBalance)
            print ("Lowest Payment: ", payment)
 
## bisection method;           
## paying debt off in a year;
#balance = 999999
#annualInterestRate = 0.18
low = balance/12
high = (balance*(1+annualInterestRate/12)**12)/12
payment = (low+high)/2
month = 0
unBalance = balance

while month < 13:
    unBalance -= payment
    unBalance *= (1+ annualInterestRate/12)
    month += 1
    if month == 12:
        if unBalance > 0.01:
            low=payment
            payment = (high+low)/2
                        
        elif unBalance < -0.01:
            high = payment
            payment = (low+high)/2
                        
        else:
            print("Lowest Payment: ", round(payment,2))
            break
        month = 0
        unBalance = balance
            
            
#        and unBalance > 0:
#        
#        payment = (payment+high)/2
#        print("highbound:", high)
#        print("low: ",payment)
#            
#    elif month==12 and unBalance < 0:
#        
#        payment = (payment+low)/2
#        print('lowbound:', low)
#        print("high: ",payment)
#    elif month == 12 and unBalance ==0:
#        print("unbalance is: ", unBalance)
#        print("Lowest Payment: ", payment)
#        break
#    month = 0
#    unBalance = balance
#        
        
       
                       
    
    





















            
        