try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"error: {e}")

print("end of program")