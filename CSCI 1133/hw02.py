import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Converts an inputted temperature in celcius to that of its fahrenheit equivalent
    Parameter(s):
        celcius: The temperature in celcius 
    Return Value:
        The new calculated value of fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
        To print a total of 25 "*" on the screen in a 5x5 array
    Parameter(s):
        There are no parameters for this function
    Return Value:
        The result of the code block within "print_25_stars" which makes 25 *s appear on the screen
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    

# Part B: Write out a few simple conversions

def area_circle(radius):
    '''
    Purpose:
        Return and print the area of a circle given an inputted radius
    Parameter(s):
        radius: the length of the radius of the circle
    Return Value:
        The value of the circle's area 
    '''
    area = (math.pi*radius**2)
    return(area)

def meters_to_feet(meters):
    '''
    Purpose:
        To convert an inputted value in meters to its equivalent in feet
    Parameter(s):
        meters: some numerical value representing the length in meters
    Return Value:
        The same meter value in feet
    '''
    feet = (meters*3.28084)
    return(feet)

def minutes_to_days(minutes):
    '''
    Purpose:
        To convert some time in minutes to its equivalent value in days
    Parameter(s):
        minutes: the length of time in minutes 
    Return Value:
        The length of time inputted in minutes in days 
    '''
    days = minutes/60/24
    return(days)

# Part C: Simulate changes in fish population over three weeks

def population(small, middle, big):
    '''
    Purpose:
        To simulate the changes in fish population given the size and return a numerical value of the population after 3 weeks of activity
    Parameter(s):
        small: number of small fish in the population
        middle: number of medium sized fish in the population
        big: number of big fish in the population
    Return Value:
        The resulting popultaion totals of the fish after 3 weeks of activity
    '''

    count = 1
    for x in range(0,3): 
        bigNew = round(big*0.9)
        middleNew = round(middle*0.95)
        smallNew = round(small*1.1)

        smallEaten = round(((.0001)*(smallNew)*(middleNew)))
        middleNew = middleNew + (smallEaten*2)
        small = smallNew - smallEaten

        middle = middleNew - round(((.0002)*(middleNew)*(bigNew)))

        big = bigNew + round(((.0002)*(middleNew)*(bigNew)))

        print("Week " + str(count) + " " + "-" + " " + "Small: " + str(small) + " " + "," + " " + "Middle: " + str(middle) + " " + "," + " " + "Big: " + str(big))

        count += 1
    return(small+middle+big)
