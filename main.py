""" Calculator"""
def add(p, q):
    return p + q
def subs(p, q):
    return p - q
def mul(p, q):
    return p * q
def div(p, q):
    return p / q


p = float(input("Please enter the first number: "))
choice = input("Please select operator(+/ -/ */ /): ")
q = float(input("Please enter the second number: "))

if choice == '+':
    print(f"{p} {choice} {q} =", add(p, q))
elif choice == '-':
    print(f"{p} {choice} {q} =", subs(p, q))
elif choice == '*':
    print(f"{p} {choice} {q} =", mul(p, q))
elif choice == '/':
    print(f"{p} {choice} {q} =", div(p, q))
else:
    print("This is an Invalid input")

