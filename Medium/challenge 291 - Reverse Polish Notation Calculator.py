"""
Challenge: Reverse Polish Notation Calculator

Description:
A little while back we had a programming challenge to convert an infix expression (also known as "normal" math) to a
postfix expression (also known as Reverse Polish Notation). Today we'll do something a little different: We will write a
calculator that takes RPN input, and outputs the result.

The input will be a whitespace-delimited RPN expression. The supported operators will be:
+ - addition
- - subtraction
*, x - multiplication
/ - division (floating point, e.g. 3/2=1.5, not 3/2=1)
// - integer division (e.g. 3/2=1)
% - modulus, or "remainder" division (e.g. 14%3=2 and 21%7=0)
^ - power
! - factorial (unary operator)
Sample input:
0.5 1 2 ! * 2 1 ^ + 10 + *

The output is a single number: the result of the calculation. The output should also indicate if the input is not a
valid RPN expression.
Sample output:
7
Explanation: the sample input translates to 0.5 * ((1 * 2!) + (2 ^ 1) + 10), which comes out to 7.

Bonus:
No Bonus

Result:
Failure.
Standard: Took about 54 minutes
First two cases work, last does not. Not sure why yet probably implementation error

Second attempt:
Success!
Standard: Took about 11 minutes.
"""

import math


def perform_calculation(num1, num2, operator):
    if operator == "+":
        return str(float(num1) + float(num2))
    elif operator == "-":
        return str(float(num1) - float(num2))
    elif operator == "/":
        return str(float(num1) / float(num2))
    elif operator == "*" or operator == "x":
        return str(float(num1) * float(num2))
    elif operator == "//":
        return str(float(num1) // float(num2))
    elif operator == "%":
        return str(float(num1) % float(num2))
    elif operator == "^":
        return str(pow(float(num1), float(num2)))
    elif operator == "!":
        return str(math.factorial(float(num2)))


def calculator(equation):
    lst = equation.split(" ")
    stack = []
    for ele in lst:
        if ele.isdigit() or ele.__contains__("."):
            stack.append(ele)
        elif ele == "!":
            num = stack.pop()
            stack.append(perform_calculation(0, num, ele))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(perform_calculation(num1, num2, ele))
    ans = float(stack[0])
    if ans.is_integer():
        return int(ans)
    return ans


print(calculator("100 807 3 331 * + 2 2 1 + 2 + * 5 ^ * 23 10 558 * 10 * + + *"))
print(calculator("50 30 20 + -"))
