try:
    value = int(input("enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("cannot divide by zero!")
else:
    print(f"the result is {result}")

print("end of program")