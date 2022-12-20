"""
Author: Amisha Manga
Date: 17/12/2022

This is the coding solution to the Fizz Buzz problem in python 3

Usage:
$ python FizzBuzzChallenge.py
"""

def vMain():
    """This is the main method of the Fizz Buzz program.
    Parameters:
    Returns:
    """
    # Get user input for an integer number
    intInputNumber = int(input("Enter an integer n"))

    # Check that user input is valid
    if intInputNumber is "":
        print("No input provided, Exiting...")
        return
    
    for i in range(1, intInputNumber+1):
        if (i%5 == 0) and (i%3 ==0):
            print("FizzBuzz")
        elif (i%3 == 0):
            print("Fizz")
        elif (i%5 == 0):
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    vMain()