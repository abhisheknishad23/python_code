num1 = int(input("Enter the number"))
num2 = int(input("Enter the second number"))

opratore = input("Enter the oprator")

match opratore:
    case "+":
        print("Sum is", num1 + num2)
    case "-":
        print("subtrack is", num1-num2)
    case "*":
        print("multiplication is: ", num1*num2)
    case _:
        print("valid operatore")