"""
Contains functions that implement the game over screen.
Month Year
First Last
First Last 
First Last 
"""

import random


def problem(coord: tuple) -> None:   
    x = int(coord[0])
    y = int(coord[1])


    # making adding and subtraction equation for Y
    first_number: int = random.randint(y+10, 20)
    positive_negative: int = random.choice(["+", "-"])


    if positive_negative == "+":
     second_number: int = y - first_number
    else:
       second_number: int = y + first_number

    wrong_right_one: int =  random.randint(1, y)
    wrong_right_two: int = random.randint(1, y) 

    equation_one: str = f"{first_number} {positive_negative} {second_number} = " 
    equations_two: str = f"{first_number} {positive_negative} {wrong_right_one} = " 
    equations_three: str = f"{first_number} {positive_negative} {wrong_right_two} = " 

    print(f"{equation_one} \
            {equations_two} \
            {equations_three}")
        


    # making adding and subtraction equation for x
    second_number: int = random.randint(1, x)
    positive_negative: int = random.choice(["+", "-"])

    if positive_negative == "+":
        first_number: int = x - second_number
    else:
        first_number: int = second_number - x

    wrong_right_one: int =  random.randint(1, x)
    wrong_right_two: int = random.randint(1, x) 

    equation_one_x: str = f"{first_number} {positive_negative} {second_number} = " 
    equations_two_x: str = f"{first_number} {positive_negative} {wrong_right_one} = " 
    equations_three_x: str = f"{first_number} {positive_negative} {wrong_right_two} = " 


    print(f"{equation_one_x} \
            {equations_two_x} \
            {equations_three_x}")
        





    
        






    
        



