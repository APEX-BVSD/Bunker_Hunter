"""
Contains functions that implement and make the equations for the equations screen.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""

from settings import *
import random

def get_equation_set(coord: int) -> dict: 
    """
    Creates a set of math equations based on the coordinate selected.

    Parameters:
    coord (int): The coordinate value used as the target answer for the equations

    Returns:
    dict: A dictionary containing the correct equation, list of all equations, and coord value
    """

    correct: str = make_equation(coord, make_correct = True)
    equations: list[str] = [
                correct,
                make_equation(coord, make_correct = False),
                make_equation(coord, make_correct = False)
    ]
    random.shuffle(equations)

    return {
        "correct" : correct,
        "equations" : equations,
        "coord" : coord
    }

def make_equation(correct_answer: int, make_correct: bool = True) -> str:   
    """
    Creates a math equation string that either equals or does not equal the correct answer.

    Parameters:
    correct_answer (int): The target answer for the equation
    make_correct (bool): If True, generates an equation that equals the correct_answer;
                     if False, generates an incorrect equation

    Returns:
    str: A formatted equation string in the form "num1 operation num2 = ?"
    """


    operation: str = random.choice(["+","-"])
    
    if make_correct:
        if operation == "+":
            low: int = LOW 
            high: int = HIGH + correct_answer
        
            first_number: int = random.randint(low, high)
            second_number: int = correct_answer - first_number
            
        else:
            low: int = LOW + correct_answer
            high: int = HIGH 
            first_number: int = random.randint(low, high)
            second_number: int = first_number - correct_answer

    else:
        if operation == "+":
            low: int = LOW 
            high: int = HIGH + correct_answer 
            first_number: int = random.randint(low, high)
            exception: int = correct_answer - first_number
            second_number: int = random.randint(low, high)
            while second_number == exception: 
                second_number: int = random.randint(low, high)

        else:
            low: int = LOW + correct_answer
            high: int = HIGH 
            first_number: int = random.randint(low, high)
            exception: int = correct_answer - first_number
            second_number: int = random.randint(low, high)
            while second_number == exception: 
                second_number: int = random.randint(low, high)     



    if first_number < 0:
        first_number = f"({first_number})"

    if second_number <0:
        second_number = f"({second_number})"
   
    return f" {first_number} {operation} {second_number} = ?"
