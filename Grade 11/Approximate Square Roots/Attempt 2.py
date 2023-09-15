# This Square Root approximation is called "Binomial Approximation."
# Input Validation
try:
    num = float(input("Enter the number to square root: "))
except:
    raise ValueError("Inputted Character is not an real number.")
    num = 1

prev_num = num # Storing original input

# Imaginary Validation:
if num < 0:
    im = 'i'
    num *= -1
else:
    im = ""

# Defining Functions
start = num


def comb(top, bottom):
    """A symbolic combination's calculator.
    Parameters:
        top (int): The total number of objects.
        botton (int): The number of choices.
    NOTE: Follows the nCr formula."""
    ans = 1
    for i in range(int(bottom)):
        ans *= (top - i)/(i + 1)
    return ans


def compute_binomial(num, no_terms, exponent = 1/2):
    """Used (1 + x) ^ 1/2 to compute square roots.
    Parameters:
        num (int): the number whose sqrt is calculated.
        no_terms: The amount of binomial terms used for calculations.
        exponent (float): The rational exponent."""
    ans = 0
    for i in range(int(no_terms)):
        part2 = ((num/2)/num**2) ** i
        part3 = ((num/2)/num**2)**(no_terms - i)
        part1 = comb(exponent, i)
        ans += part1 * part2 * part3
    return ans * num
guess = compute_binomial(start, 100)
print(f"You inputted {prev_num}. It's square root is {guess}{im}.")