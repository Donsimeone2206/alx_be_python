number1= int(input("Enter the first number: "))
number2= int(input("Enter the Second number: "))
operation= input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        result = number1 / number2
        if (number2==0):
            print("can't divide a number by zero")
    case _:
        print("choose operations ")
print("The result is", result)
