"""A Module containing the Newton Square Root Approximation Class."""
from termcolor import colored
class Sqrt(object):
  def __init__(self, program_details) -> None:
    self.length = 1
    self.numerical_input = 1
    self.got_input = False
    self.input_message = "\rEnter the number to square root: "
    self.string_input = "1"
    print(colored(program_details, "green"))
    self.is_int = False
    self.cond = False

  def get_input(self):
    while not self.got_input:
      in_num = input(self.input_message)
      try:
        self.string_input = in_num
        self.string_input1 = self.string_input
        self.numerical_input = float(in_num)
        self.got_input = True
        self.input_message = "\rEnter the number to square root: "
      except:
        print(f"Incorrect value supplied. Previous Entered Values: {ins}")
        self.input_message = "\rPlease enter a NUMERIC value to square root: "
    self.original_input = self.numerical_input
  
  def check_negative(self, allowed = True):
    if self.numerical_input < 0 and allowed:
      self.end_message = 'i, which is an imaginary number'
      self.numerical_input *= -1
      self.length = 2
    elif self.numerical_input > 0:
      self.end_message = ""
    else:
      print("Negative values are not allowed.")
      self.input_message = "\r Please enter a POSITIVE NUMERIC value to square root: "
      self.get_input()
      
    self.sqrt = self.numerical_input

  @staticmethod
  def one_round(num: float, guess: float):
    """Defines one round of newton's approximation.
    Parameters:
        num (float): The number you want to square root.
        guess (float): A starting number.
    """
    return (num / guess + guess) / 2
  
  def calc(self, tolerance: float = 1e-11):
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
          self.string1_num = self.string_input
          self.string_input = self.original_input
      else:
        self.cond = True

  def determine_rationality(self):
    lenght_of_input = len(self.string_input) if not self.cond else len(str(int(self.string_input)))
    if not self.cond and self.end_message != "i, which is an imaginary number":
      lenght_of_sqrt = lenght_of_input/2 + 1
      if len(str(float(self.sqrt_copy))) != lenght_of_sqrt:
        return False
      else:
        return True
    elif self.cond and self.end_message != "i, which is an imaginary number":
      return True
    else:
      return 100

  def finalize_end(self):
    if isinstance(self.determine_rationality(), bool) and self.determine_rationality():
      self.end_message = ", which is an rational number"
      self.appro = ""
    elif not self.determine_rationality():
      self.end_message = ", which is an irrational number"
      self.appro = "approximately "
    elif self.determine_rationality() == 100:
      im = ", which is an complex number"
      self.appro = "approximately "

  def __call__(self):
    self.get_input()
    self.check_negative()
    self.calc()
    self.check_int()
    self.determine_rationality()
    self.finalize_end()
    print(
    f"\n\nYou inputted {self.string_input}.\nIt's square root is {self.appro}{self.sqrt}{self.end_message}."
)