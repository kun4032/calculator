print(" hello user this program will calculate numbers for you ")

print("you can add, subtract multiply or divide tow numbers")
while True:
    try:
        num1 = float(input("enter the first number to calculate"))
        num2 = float(input("enter the second number to calculate"))
    except ValueError:
        print("invalid input, please enter valid numbers")
        continue

    print("what do u want to do with these numbers?")
    print("1 = add")
    print("2 = subtract")
    print("3 = multiply")
    print("4 = divide")
    print("5 = exit")

    choice = input("enter your choice (1/2/3/4/5): ")

    if choice == '1':
        result = num1 + num2
        print("The result of adding", num1, "and", num2, "is", result)

    elif choice == '2':
        result = num1 - num2
        print("the result of subtracting", num2, "from", num1, "is", result)

    elif choice == '3':
        result = num1 * num2
        print("the result of multiplying", num1, "and", num2, "is", result)

    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("the result of dividing", num1, "by", num2, "is", result)
        else:
            print("Error: Division by zero is not allowed.")

    elif choice == '5':
        print("Exiting the program, goodbye!")
        break

    else:
        print("invalid choice, please try again.")