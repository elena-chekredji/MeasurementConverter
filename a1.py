# -*- coding: utf-8 -*-
"""
@author: Elena Chekredji 501133464
"""
#   In my spare time, I like to cook a lot; however, many recipes use measurements
#   such as cups, teaspoons, tablespoons, oz, etc. I am unfamiliar with the conversion for 
#   some of these measurements and others seem unprecise to me (a cup of flour can be anywhere  
#   between 100-300 grams approximately of flower based on how you fill it up). Therefore I will 
#   make a program/calculator that will allow me to input any measurement and will
#   return everything in grams. 

def cups (fraction, kind = "standard"):
    if kind == "standard":
        in_g = round(fraction * 128)  # in_g is the variable which will store the finale value in grams
        # It is rounded because on a kitchen scale there are no decimals and the round function can appropriately round up or down
        s = str(in_g) + ' grams' 
        # s is a string which concatenates the value of in_g (which was casted to a string so it can be concatenates) together with the string 'grams' 
        return s
    elif kind == 'flour':
         in_g = round(fraction * 120)
         s = str(in_g) + ' grams'
         return s
    elif kind == 'sugar':
        in_g = round(fraction * 201)
        s = str(in_g) + ' grams'
        return s
    elif kind == 'liquids':
        in_g = round(fraction * 240)
        s = str(in_g) + ' grams'
        return s
    elif kind == 'butter':
        in_g = round(fraction * 240)
        s = str(in_g) + ' grams'
        return s
    else:
        s = 'You inputted none of the options'
        return s
#   This is a function which takes 2 inputs, one of which is set to standard, so it has to at least get 1 input but it can also take 2 inputs
#   Different ingredients have different weights so my function has values for the most common 4 (flour, sugar, butter and liquids)
#   It also has a standard 1 cup weight
#   The function checks which kind the ingredient is and multiplies the fraction of the cup by the weight in grams so it can calculate 1/2 a cup or 2 cups etc.

def teaspoon (fraction = 1):
    in_g = round(fraction * 4.2)
    s = str(in_g) + ' grams'
    return s
# This function only takes one input which is set to 1 and it will return a concatenated string of the value of the fraction multiplied by a teaspoon, and the string 'grams'

def tablespoon (fraction = 1):
    in_g = round(fraction * 14.3)
    s = str(in_g) + ' grams'
    return s
# This function only takes one input which is set to 1 and it will return a concatenated string of the value of the fraction multiplied by a tablespoon and the string 'grams'

def oz (how_many):
    in_g = round(how_many * 28.3)
    s = str(in_g) + ' grams'
    return s
# This function returns a concatenated string s of the converted ounces to grams and the string 'grams'

def pound (how_many):
    g = round(453.6 * how_many)
    s = str(g) + ' grams'
    return s
# This function returns a rounded version of the conversion from pounds to grams

def fahrenheit_conv (degrees):
    celsius = round((degrees-32)*(5/9))
    s = str(celsius) + '°C'
    return s 
# This function converts Fahrenheit to Celsius using a conversion equation and rounds the result to an integer
# In the next line it converts Celsius to a string and concatenates it with the string '°C'
# It then returns the concatenated string s

# It doesn't matter that I used the same variable names such as s or in_g in all the previous functions because variables inside functions are in the local scope 
# Variable in the local scope only exist within the function 


# My main program begins here
print("Hello, I am a calculator that will help you with your cooking! What would you like to convert today?")
print("To convert cups to grams write 'cups' and then press enter!")
print("To convert tablespoons to grams enter 'tbs'!")
print("To convert teaspoons to grams enter 'tsp'!")
print("To convert ounces to grams enter 'oz'!")
print("To convert pounds to grams enter 'pounds'!")
print("To convert Fahrenheit to Celsius enter 'F'!")
# These print statements inform the user of what they need to imput in order to convert their values

keep_asking = True
# This is a boolean variable which will allow me to run the while loop as many times as the user needs until its value is changed to false

while keep_asking == True:
# This wile loop will keep asking the user what they want to convert until they say they are done and input 'done'
    usr_input = input("Enter what you would like to convert: ")
    if usr_input == 'cups':
    # This if statements checks the user input against the string ' cups' to see if the user wants to convert from cups. If so it enters the if statement.
        print("Enter the fraction of the tablespoon that you want!")
        print("Example: If you want 1/2 cup, 1 is the numerator, 2 is the denominator.")
        nume = int(input("Enter the numerator: "))
        den = int(input("Enter the denominator: "))
        fract = nume/den
        # Here i get the user to input the numerator and the denominator in order to create the fraction because python cannot cast the input 1/2 into a float 
        # So in order for the user not to input decimals, I create the fraction out of the numerator and the denominator 
        kind = input("Would you like to specify what you are converting, if so: enter 'flour', 'sugar', 'liquids', 'butter' or enter 'nul' for the standard cup conversion: ")
        if kind == 'nul':
            # I check if the user wants to use the standard value for the cup and if that is the case it calls the cups function with only the fraction value
            # I can do this because the variable kind has a predefined value in the definition of the function which allows me to be called with one variable
            print(cups(fract) + "\n")   
            # I add in a new line to separate my answer from the line of code that tells the user that if they are done they should enter 'done' so it's clearer
            print("If you are done and don't have any more values to convert enter 'done'!")
        else:
            # If the user wants a fraction of a cup then the function is called with both of the values that the user inputted
            print(cups(fract, kind) + "\n")
            print("If you are done and don't have any more values to convert enter 'done'!")
    elif usr_input == 'tsp':
        # This if statements checks the user input against the string ' tbs' to see if the user wants to convert from teaspoons. If so it enters the if statement.
        print("Enter the fraction of the teaspoon that you want!")
        print("Example: If you want 1/2 teaspoon, 1 is the numerator, 2 is the denominator.")
        nume = int(input("Enter a numerator: "))
        den = int(input("Enter a denominator: "))
        if nume == 1 and den == 1:
            # I check if the numerator and the denominator are both equal to 0. If this is the case i call the unction with no variable because the function has a 
            # predefined value for the fraction which is 1
            print(teaspoon() + "\n")
            print("If you are done and don't have any more values to convert enter 'done'!")
        else:
            # If the numerator and denominator are not equal to 1 then it calls the function with the value fract
            fract = nume/den
            print(teaspoon(fract) + "\n")
            print("If you are done and don't have any more values to convert enter 'done'!")
    elif usr_input == 'tbs':
        # This code is the same as for the teaspoon
        print("Enter the fraction of the tablespoon that you want!")
        print("Example: If you want 1/2 tablespoon, 1 is the numerator, 2 is the denominator.")
        nume = int(input("Enter the numerator: "))
        den = int(input("Enter the denominator: "))
        if nume ==1 and den == 1:
            print(tablespoon() + "\n")
            print("If you are done and don't have any more values to convert enter 'done'!")
        else:
            fract = nume/den
            print(tablespoon(fract) + "\n")
            print("If you are done and don't have any more values to convert enter 'done'!")
            # Here it is the same as teaspoon 
    elif usr_input == 'oz':
        num = float(input("How many ounces do you need to convert? "))
        # I store the user input in num(how many ounces the user wants to convert) and then I call the unction with it. It takes a float input in case the value is 14.7 ounces
        print(oz(num)+ "\n")
        print("If you are done and don't have any more values to convert enter 'done'!")
    elif usr_input == 'pounds':
        value = float(input("How many pounds do you want me to convert to grams? "))
        print(pound(value)+ "\n")
        print("If you are done and don't have any more values to convert enter 'done'!")
        # Takes in a float input that is stored in value and calls the function pound with value and prints the result
    elif usr_input == 'F' or usr_input == 'f':
        # I added the 'f' check in case the user forgets that capitalization matters. This way they will still get their result
        C = float(input("How many Fahrenheit do you want me to convert to Celsius? "))
        print(fahrenheit_conv(C)+ "\n")
        print("If you are done and don't have any more values to convert enter 'done'!")
        # Takes in a float input and calls the function fahrenheit_conv with it and prints the result
    elif usr_input == 'done':
        keep_asking = False
        # if the user inputs done it changes the value of keep_asking to false which breaks the loop because it will fail the (while keep_asking == True) condition
    else:
        print("Your input was none of the options please try again!")
        # If the user inputs something that my program cannot convert from it tells them to try again 

print("Thank you for using my conversion app, to convert again, start the program again!")
# It will execute once before the end of my program and will thank the user for using my program





























    
    

