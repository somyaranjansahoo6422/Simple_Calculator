def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select Operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter Choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError("Can't Divide By Zero")
                print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError:
            print("Invalid Input! Please Enter A Number.")
            continue
        except ZeroDivisionError as e:
            print(e)
            continue
        next_calculation = input("Are You Interested In Next Calculation?[YES(Y)/NO(N)]:")
        if next_calculation == "N":
            break
        elif next_calculation == "n":
            break
    else:
        print("You Entered A Invalid Input")
