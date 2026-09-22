try:
    value = int(input("enter a number: "))
    result = 10 / value
except ValueError:
    print("invalid input please enter a bumber.")
except ZeroDivisionError:
    print("cannot divide by zero!")
else:
    print(f"the result is {result}")
finally:
    print("execution completed.")

print("end of program")