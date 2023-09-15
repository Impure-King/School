# This Square Root approximation is called "Newton's Approximation."
length = 1
num = 1
# Input Validation
input_cond = True
start_input_message = "Enter the number to square root: "
string_num = "1"
while input_cond:
  ins = input(start_input_message)
  try:
    string_num = ins
    string_num1 = string_num
    num = float(ins)
    input_cond = False
    start_input_message = "Enter the number to square root: "
  except:
    print(f"Incorrect value supply. Previous Entered Value: {ins}")
    start_input_message = "Please enter a NUMERIC value to square root: "

prev_num = num  # Storing original input

# Imaginary Validation:
if num < 0:
  im = 'i, which is an imaginary number'
  num *= -1
  length = 2
else:
  im = ", which is a real number"

# Definiting functions
guess = num


def one_round(num: float, guess: float):
  """Defines one round of newton's approximation.
    Parameters:
        num (float): The number you want to square root.
        guess (float): A starting number.
    """
  return (num / guess + guess) / 2


def calc(guess: float, tolerance: float = 0.0000000001, num: float = num):
  """Defines the loop that optimizes the approximation.
    Parameters:
        guess (float): The number to start optimizing.
        tolerance (float): The prevision the answer should be.
        num (float): The original number to square root.
    """
  while abs(guess**2 - num) > tolerance:
    guess = one_round(num, guess)
  return guess


def analyse_num(num: str):
  ind = num.find('.')
  for i in num[ind + 1:]:
    if i != '0' and ind != -1:
      return False
  return True


# Printing guess
guess = calc(guess)
is_int = False
# Converting to int
guess1 = f"{guess:.10f}"
# guess1 = "%.10f" % guess
cond = False

# Handling Integer Conversion:

if int(float(guess1)) == float(guess1):
  if len(string_num) != length:
    if not analyse_num(string_num):
      cond = False
    else:
      cond = True
      string1_num = string_num
      string_num = prev_num
  else:
    cond = True

if cond:
  guess1 = int(guess)
print(f"\n\nYou inputted {string_num}.\nIt's square root is {guess1}{im}.")

# Determine Irrationality and Rationality:
def determine(str_num:str = string_num, sqr:str = guess1):
  global im
  length_of_input = len(string_num) if not cond else len(str(int(string_num)))
  if not cond and im != "i, which is an imaginary number":
    length_of_sqrt = length_of_input/2 + 1
    if len(str(float(sqr))) != length_of_sqrt:
      print("The answer is irrational.")
    else:
      print("The answer of rational.")
  elif cond and im != "i, which is an imaginary number":
    print("The answer is rational.")
determine()