"""
Contains functions that implement the game over screen.
Month Year
First Last
First Last 
First Last 
"""
from settings import *
import random

def get_equation_set(coord: tuple) -> dict:
    correct_x: str = make_equation(coord[0], make_correct = True)
    equations_x: list[str] = [
                correct_x,
                make_equation(coord[0], make_correct = False),
                make_equation(coord[0], make_correct = False)
    ]
    random.shuffle(equations_x)


    correct_y: str = make_equation(coord[1], make_correct = True),
    equations_y: list[str] = [
                correct_y,
                make_equation(coord[1], make_correct = False),
                make_equation(coord[1], make_correct = False)
    ]
    random.shuffle(equations_y)

    return {
        "correct_x" : correct_x,
        "equations_x" : equations_x,
        "correct_y" : correct_y,
        "equations_y" : equations_y
    }

def make_equation(correct_answer: int, make_correct: bool = True) -> str:   
    """
    What is does
    Parameters
    correct_answer(int): Describe
    make_correct(bool): Describe
    
    Returns:
    str: Describe
    """

    operation: str = random.choice(["-","-"])
    
    if make_correct:
        if operation == "+":
            low: int =  LOW 
            high: int = HIGH + correct_answer
        
            first_number: int = random.randint(low, high)
            second_number: int = correct_answer - first_number
            
        else:
            low: int =  LOW + correct_answer
            high: int = HIGH 
            first_number: int = random.randint(low, high)
            second_number: int = first_number - correct_answer

    else:
        if operation == "+":
            low: int =  LOW 
            high: int = HIGH + correct_answer 
            first_number: int = random.randint(low, high)
            exception: int = correct_answer - first_number
            second_number: int = random.randint(low, high)
            while second_number == exception: 
                second_number: int = random.randint(low, high)

        else:
            low: int =  LOW + correct_answer
            high: int = HIGH 
            first_number: int = random.randint(low, high)
            exception: int = correct_answer - first_number
            second_number: int = random.randint(low, high)
            while second_number == exception: 
                second_number: int = random.randint(low, high)     

    return f"{first_number} {operation} {second_number} = ?"



    
        






    
        



