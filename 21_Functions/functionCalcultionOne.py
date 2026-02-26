def calulate(num1, num2, op):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == 'x':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("Invalid operation")


calulate(10,10,'+')
calulate(10,10,'-')
calulate(10,10,'x')
calulate(10,10,'/')

calulate(10,10,'%')