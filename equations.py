"""
Contains functions that implement the game over screen.
Month Year
First Last
First Last 
First Last 
"""
from settings import *
import random


def mode_1_problem(correct_answer: int, make_correct: bool = True) -> str:   
    """
    What is does
    Parameters
    correct_answer(int): Describe
    make_correct(bool): Describe
    
    Returns:
    str: Describe
    """

    operation: str = random.choice(["+","-"])
    
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

    return f"{first_number} {operation} {second_number}"

#def mode_2_problem(correct_answer: int, make_correct: bool = True) -> str:

    operation: str = random.choice(["*","/"])
    
    if make_correct:
        if operation == "*":
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
        if operation == "*":
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

    return f"{first_number} {operation} {second_number}"


    
        






    
        



