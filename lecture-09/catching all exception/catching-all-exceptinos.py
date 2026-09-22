try:
    value = int(input("enter a number: "))
    result = 10 / value
except Exception as e: #เก็บ ข้อความเออเร่อในตัวแปร e
    print(f"an error occurred: {e}")

print("end of program")