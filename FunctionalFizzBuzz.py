"""
Created on Mon May 28 14:09:18 2018
FunctionalFizzBuzz
@author: Utility
"""

def FizzBuzz(x,fzr=3,bzr=5):
    """
    Will report "Fizz" for a number which 
    is divisible by fzr, "Buzz" for a number
    which is divisible by bzr, and "FizzBuzz" 
    for a number divisible by both, these 
    default to 3, and 5 in the
    absence of inputs. if not divisible by either
    returns x
    """
    if x % fzr == 0 and x % bzr == 0:
        print ("FizzBuzz")
        return "FizzBuzz"
    elif x % fzr == 0:
        print ("Fizz")
        return "Fizz"
    elif x % bzr == 0:
        print ("Buzz")
        return "Buzz"
    else:
        print (x)
        return x
