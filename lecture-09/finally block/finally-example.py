try:
    numerator = float(input("enter the numerator: "))
    denominator = float(input("enter the denominator: "))

    result = numerator / denominator
    print(f"the result is : {result}")

except ZeroDivisionError:
    print("error: you cannot divide by zero. ")
except ValueError:
    print("error: invalid input please enter numeric values.")

finally:
    print("execution completed, whether an exception occurred or not.")

print("end of program")