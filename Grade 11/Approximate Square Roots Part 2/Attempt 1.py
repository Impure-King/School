# This Square Root approximation is called "Newton's Approximation."
import sys
num = 1
# Input Validation of number:
input_cond = True
start_input_message = "Enter the number to square root: "
while input_cond:
    ins = input(start_input_message)
    sys.stdout.write("\033[F") 
    try:
        num = float(ins)
        input_cond = False
        start_input_message = "Enter the desired precision of the sqrt: "
    except:
        print(f"Incorrect value supply. Previously Entered Value: {ins}")
        # sys.stdout.write("\033[F") 
        start_input_message = "Please enter a NUMERIC value to square root: "


# Input Validation of Precision:
# input_cond = True
# while input_cond:
#     print("The ")
#     ins = input(start_input_message)
#     try:
#         num = float(ins)
#         input_cond = False
#         start_input_message = "Enter the number to square root: "
#     except:
#         print(f"Incorrect value supply. Previous Entered Value: {ins}")
#         start_input_message = "Please enter a NUMERIC value to square root: "

prev_num = num # Storing original input

# Imaginary Validation:
if num < 0:
    im = 'i, which is an imaginary number'
    num *= -1
else:
    im = ", which is a real number"

# Definiting functions
guess = num
def one_round(num:float, guess:float):
    """Defines one round of newton's approximation.
    Parameters:
        num (float): The number you want to square root.
        guess (float): A starting number.
    """
    return (num/guess + guess)/2
def calc(guess:float, tolerance:float = 0.000000001, num:float = num):
    """Defines the loop that optimizes the approximation.
    Parameters:
        guess (float): The number to start optimizing.
        tolerance (float): The prevision the answer should be.
        num (float): The original number to square root.
    """
    while (guess**2 - num) > tolerance:
        guess = one_round(num, guess)
    return guess

# Printing guess
guess = calc(guess)
print(f"\n\nYou inputted {prev_num}. It's square root is {guess}{im}.")