''' A function is a block of code that performs a specific task whenever it is called. in bigger problems, where
we have large amounts of code, it is a adviasble to create or use exicting functions that make the program flow organized and neat.

there are two types of functions:

1. built in functions 
2. user defined functions

Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:
def function_name(parameters):
  pass
  # Code and Statements

Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
Any parameters and arguments should be placed within the parentheses.
Rules to naming function are similar to that of naming variables.
Any statements and other code within the function should be indented.

'''

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

    def isGreater(a,b):
        if(a>b):
         print("First number is greater")
        else:
          print("second number is greater or equal")
        
        def isLesser(a,b):
           pass

        a = 9
        b = 8
        isGreater(a,b)
        calculateGmean(a,b)
        c=8
        d=74
        isGreater(c,d)
        calculateGmean(c,d)

