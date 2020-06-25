def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    num1, operator, num2 = calculation.split(' ')
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        raise
    if operator not in '+-*/' or (operator == '/' and num2 == 0):
        raise ValueError
    
    if operator == '+':
       return num1 + num2
    elif operator == '-':
       return num1 - num2
    elif operator == '*':
       return num1 * num2
    else:
       return round(num1 / num2, 2)
