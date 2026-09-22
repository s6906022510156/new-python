try:
    value = int(input("enter a number: "))
    result = 10 / value
except ValueError:
    print("invalid input please enter a number")
except ZeroDivisionError:
    print("cannot divide by zero")

print("end of program")