number1=float(input('Enter first number'))
number2 = float(input('Enter first number'))
operator = input('Enter operation(+, -, *, /):')

if operator == '+':
    result = number1+number2
elif operator == '-':
    result = number1-number2
elif operator == '*':
    result = number1*number2
elif operator == '-':
    result = number1/number2
else:
    result='incorrct'

# print result
print(f'{number1} {operator} {number2} = {result}')