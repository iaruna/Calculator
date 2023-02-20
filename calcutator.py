n = int(input("Enter 1st number: "))
m = int(input("Enter 2nd number: "))
operation = input("Enter operation: ")

if operation == "+":
    print(f"Addition of {n} + {m} is {n+m}")
elif operation == "-":
    print(f"Subtraction of {n} - {m} is {n - m}")
elif operation == "*":
    print(f"Multiply of {n} * {m} is {n * m}")
elif operation == "/":
    print(f"Divide of {n} / {m} is {n / m}")
elif operation == "%":
    print(f"Module of {n} % {m} is {float(n % m)}")
elif operation == "//":
    print(f"FloorDivision of {n} // {m} is {float(n // m)}")
else:
    print("provide correct details only number & operator")
