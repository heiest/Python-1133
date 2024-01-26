import math

def glorious(val):
    '''
    Purpose: 
    To create a loop that checks a number and whether that number is divisible by any number from 10 to 50 and then labels that number as either glorious or not
    Parameter(s):
    -val: stores the input that the function takes in, and therefore is the number that is checked if it is glorious or not
    Return Value(s):
    Returns true of false depending on if the number that is inputted is divisible by any number from 10 to 50
    '''
    count = 10
    while val % count > 0:
        if val % count == 0:
            return False
        elif count == 50:
            return True
        count +=1
    return False



def count_glorious(low, high):
    '''
    Purpose:
    To take in two integers and check to see how many "glorious" numbers exists within the bounds of both numbers with the exception of returning 0 when the first input is greater than the 2nd
    Parameter(s):
    -low: the lower number of the specified bound in which glorious numbers will be tallied
    -high: the higher number of the specified boun dinwhich glorious numbers will be tallied
    Return Value:
    Returns the number of how many glorious numbers are within the specified bound, returns 0 if the lower bound is higher than the higher bound
    '''
    count = 0
    if low > high:
        return 0
    for x in range(low,high+1):
        if glorious(x) ==  True:
            count = count + 1
    return count


def durdle_match(guess, target):
    '''
    Purpose:
    To analyze the index values of a guess and target string, and to return a string consisting of B,G,Y depending on if the specific index value is incorrect, correct, or partially correct
    Parameter(s):
    -guess: The five letter string representing the users guess at the target string 
    -target: The five letter string that the user's guess string is being compared to
    Return Value:
    A five character string consisting of B,G,Y that is the result of comparing the two strings and finding if the characters guessed are present in the target or not
    '''

    checker = 0
    bgy = ""
    for x in range(0,len(target)):
        if guess[x] == target[x]:
            bgy = bgy + "G"
        elif guess[x] != target[x]:
            for y in range(0,len(target)):
                if guess[x] == target[y]:
                    checker = 1
            if checker == 1:
                bgy = bgy + "Y"
            else :
                bgy = bgy + "B"
            checker = checker - 1
    return bgy


def durdle_game(target):
    '''
    Purpose:
    Use the durdle_match function to make a game that has the user guess a target value until the user guesses the correct string
    Parameter(s):
    -target: the inputted target string that the user will guess until correctly identifying
    Return Value:
    Returns the total amount of guesses it took the user to correctly identify the target string
    '''

    count = 1
    print('Welcome to Durdle!')
    string1 = durdle_match(str(input('Enter a Guess:')),target)
    print(string1)

    while string1 != "GGGGG":
        string1 = durdle_match(str(input('Enter a Guess:')),target)
        print(string1)
        count +=1
    print("Congratulations, you got it in " + str(count) + " guess(es)!")
    return count



    
        
        