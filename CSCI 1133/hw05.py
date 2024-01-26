import math

def closest(vals):
    '''
    Purose:
    To compare all the values in a list of random integer values and output the smallest difference between any two random pairs of integers within the list
    Parameter(s):
    - vals: is the random list that contains all the integer values
    Return Value(s):
    A number representing the smallest difference between any of the pairs that exists within the list
    '''

    start = math.fabs(vals[0]-vals[1])
    for num1 in vals:
        for num2 in vals:
            if num1 != num2:
                temp = math.fabs(num1-num2)
                if temp < start:
                    start = temp
    return int(start)



def change_key(notes, up):
    '''
    Purpose:
    Given a list of strings representing notes, and an integer representing the amount of steps up an octave you want to go, return a new string represting the original shifted according to the scale provided
    Parameter(s):
    - notes: notes is the list of strings representing a bunch of notes that are inputted
    - up: the integer value representing how many steps up or down the octave each note needs to be shifted according to the original scale
    Return Value(s):
    A new list of strings or notes that are shifted according to the set integer and in reference to the scale provided
    '''
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    shifted = []
    for x in range(len(notes)):
        for y in range(len(scale)):
            if notes[x] == scale[y]:
                step = y + up
                if abs(step) < len(scale):
                    shifted.append(scale[step])
                else:
                    step = step % 12
                    shifted.append(scale[step])
    return shifted



def avoid_sz(names_list):
    '''
    Purpose:
    To create a function that rearranges a list of names such that all of the strings at odd indexes do not contain 's','z','S','Z'
    Parameter(s):
    - names_list: the list of names inputted into the function that will be changed
    Return Value(s):
    Returns a new list of strings that has been rearranged such that all odd indexes have strings that do not contain any of the above characters
    Also returns "impossible" if there are too many occurances of s or z names that they cannot be removed from odd indexes
    '''
    finalNames = []
    sznames = []
    nosz = []
    sznamecount = 0
    for x in range(len(names_list)):
        if 's' in names_list[x] or 'z' in names_list[x] or 'S' in names_list[x] or 'Z' in names_list[x]:
            sznamecount +=1
    if sznamecount > (len(names_list)/2):
        print("Impossible: Too many s/z names")
        return nosz
    
    for i in range(len(names_list)):
        word = names_list[i]
        if 's' not in word and 'z' not in word and 'S' not in word and 'Z' not in word:
            nosz.append(names_list[i])
    for j in range(len(names_list)):
        temp = names_list[j]
        if 's' in temp or 'z' in temp or 'S' in temp or 'Z' in temp:
            sznames.append(names_list[j])
    while nosz != []:
        finalNames.append(nosz.pop())
        if sznames != []:
            finalNames.append(sznames.pop())
    return finalNames