first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)


