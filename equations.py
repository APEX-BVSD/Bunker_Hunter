"""
Contains functions that implement the game over screen.
Month Year
First Last
First Last 
First Last 
"""

import random

def problem() -> None:   
    y: int = int(input())
    x: int = int(input()) 


    # making adding and subtraction equation for Y
    second_number: int = random.randint(1, 10)
    positive_negative: int = random.choice(["+", "-"])
    second_number: int

    if positive_negative == "+":
     first_number: int = y - second_number
    else:
        first_number: int = second_number - y

    wrong_right_one: int =  random.randint(1, 10)
    wrong_right_two: int = random.randint(1, 10) 

    equation_one: str = f"{second_number} {positive_negative} {first_number} = " 
    equations_two: str = f"{second_number} {positive_negative} {wrong_right_one} = " 
    equations_three: str = f"{second_number} {positive_negative} {wrong_right_two} = " 

    if second_number - positive_negative and positive_negative < 0:
        equation_one = second_number + positive_negative and positive_negative *-1
        equation_two = second_number + positive_negative and positive_negative *-1
        equation_three = second_number + positive_negative and positive_negative *-1


    print(f"{equation_one} \
            {equations_two} \
            {equations_three}")
        


    # making adding and subtraction equation for x
    second_number: int = random.randint(1, 10)
    positive_negative: int = random.choice(["+", "-"])
    second_number: int

    if positive_negative == "+":
        first_number: int = x - second_number
    else:
        first_number: int = second_number - x

    wrong_right_one: int =  random.randint(1, 10)
    wrong_right_two: int = random.randint(1, 10) 

    equation_one: str = f"{second_number} {positive_negative} {first_number} = " 
    equations_two: str = f"{second_number} {positive_negative} {wrong_right_one} = " 
    equations_three: str = f"{second_number} {positive_negative} {wrong_right_two} = " 

    if second_number - positive_negative and positive_negative < 0:
        equation_one_x = second_number + positive_negative and positive_negative *-1
        equation_two_x = second_number + positive_negative and positive_negative *-1
        equation_three_x = second_number + positive_negative and positive_negative *-1


    print(f"{equation_one_x} \
            {equation_two_x} \
            {equation_three_x}")
        





    
        






    
        



