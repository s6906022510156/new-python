subject1 = input("Enter the score for test 1: ")
subject2 = input("Enter the score for test 2: ")
subject3 = input("Enter the score for test 3: ")

total = subject1 + subject2 + subject3
print(total)
if total / 3 > 95:
    print("congratulation ! that is a great average")
