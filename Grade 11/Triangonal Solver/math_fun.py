"""A Module containing the Newton Square Root Approximation Class."""
from termcolor import colored
from numba import njit

# Square Root Object:
class Sqrt(object):
  prompt_print = False

  def __init__(
      self,
      program_details="A Function that calculates the square root of a positive real number.\n\n",
      input_message="Enter the number to square root: ") -> None:
    self.length = 1
    self.numerical_input = 1
    self.got_input = False
    self.input_message = input_message
    self.string_input = "1"
    if not Sqrt.prompt_print:
      print(colored(program_details, "green"))
      Sqrt.prompt_print = True
    self.is_int = False
    self.cond = False

  def get_input(self, inputs=None, string_input=None):
    while not self.got_input:
      in_num = input(self.input_message) if inputs is None else inputs
      try:
        self.string_input = str(
            in_num) if string_input is None else string_input
        self.string_input1 = self.string_input
        self.numerical_input = float(in_num)
        self.got_input = True
        self.input_message = "Enter the number to square root: "
      except:
        print(f"Incorrect value supplied. Previous Entered Values: {in_num}")
        self.input_message = "Please enter a NUMERIC value: "
    self.original_input = self.numerical_input
    return self.numerical_input, self.string_input

  def check_negative(self, allowed=True):
    if self.numerical_input < 0 and allowed:
      self.end_message = 'i, which is an imaginary number'
      self.numerical_input *= -1
      self.length = 2
    elif self.numerical_input >= 0:
      self.end_message = ""
    else:
      print("Negative values are not allowed.")
      self.input_message = "Please enter a POSITIVE NUMERIC value: "
      self.got_input = False
      self.input_validation(allowed, self.numerical_input, self.string_input)

    self.sqrt = self.numerical_input

  @staticmethod
  @njit
  def one_round(num: float, guess: float):
    """Defines one round of newton's approximation.
    Parameters:
        num (float): The number you want to square root.
        guess (float): A starting number.
    """
    return (num / guess + guess) / 2

  def calc(self, tolerance: float = 1e-10):
    """Defines the loop that optimizes the approximation.
    Parameters:
        guess (float): The number to start optimizing.
        tolerance (float): The prevision the answer should be.
        num (float): The original number to square root.
    """
    while abs(self.sqrt**2 - self.numerical_input) > tolerance:
      self.sqrt = self.one_round(self.numerical_input, self.sqrt)
    self.sqrt_copy = f"{self.sqrt:.10f}"
    return self.sqrt

  def analyse_num(self, num):
    ind = num.find('.')
    for i in num[ind + 1:]:
      if i != '0' and ind != -1:
        return False
    return True

  def check_int(self):
    if int(float(self.sqrt_copy)) == float(self.sqrt_copy):
      if len(self.string_input) != self.length:
        if not self.analyse_num(self.string_input):
          self.cond = False
        else:
          self.cond = True
          self.string_input1 = self.string_input
          self.string_input = self.original_input
      else:
        self.cond = True

  def determine_rationality(self):
    lenght_of_input = len(self.string_input) if not self.cond else len(
        str(int(self.string_input)))
    if not self.cond and self.end_message != "i, which is an imaginary number":
      lenght_of_sqrt = lenght_of_input / 2 + 1
      if len(str(float(self.sqrt_copy))) != lenght_of_sqrt:
        return False
      else:
        return True
    elif self.cond and self.end_message != "i, which is an imaginary number":
      return True
    else:
      return 100

  def finalize_end(self):
    if isinstance(self.determine_rationality(),
                  bool) and self.determine_rationality():
      self.end_message = ", which is an rational number"
      self.appro = ""
    elif not self.determine_rationality():
      self.end_message = ", which is an irrational number"
      self.appro = "approximately "
    elif self.determine_rationality() == 100:
      im = ", which is an complex number"
      self.appro = "approximately "

  def convert_int(self):
    if self.cond:
      self.sqrt_copy = int(self.sqrt)

  def input_validation(self,
                       negatives_allowed=True,
                       inputs=None,
                       string_inputs=None):
    self.get_input(inputs, string_inputs)
    self.check_negative(negatives_allowed)
    return self.numerical_input, self.string_input1

  def __call__(self,
               negatives_allowed=True,
               inputs=None,
               string_inputs=None,
               print_output=True):
    """Receives the input and calculates the square root.
    Arguments:
      - condition (bool): A boolean denoting whether imaginary numbers should be considered."""
    self.input_validation(negatives_allowed, inputs, string_inputs)
    self.calc()
    self.check_int()
    self.convert_int()
    self.determine_rationality()
    self.finalize_end()
    if print_output:
      print(
          f"\n\nYou inputted {colored(self.string_input1, 'green')}.\nIt's square root is {self.appro}{colored(self.sqrt_copy, 'blue')}{self.end_message}."
      )
    else:
      return self.sqrt_copy


# Adding Pythagorean Function:
def pythagorean_theorem(a, b):
  return a**2 + b**2


def pythagorean_theorem_converse(a, b):
  return max(a, b)**2 - min(a, b)**2
