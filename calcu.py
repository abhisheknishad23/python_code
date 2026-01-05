num1 = float(input("Enter your number"));
num2 = float(input("Enter your secod number"));

choice = input("enter your choice - + * ")

if choice == "+":
    print(f"Adition:{num1+num2}")
elif choice == "-":
    print(f"subtraction:{num1-num2}")
elif choice == "*":
    print(f"multiplication:{num1*num2}")
else:
    print("invalid choice")
