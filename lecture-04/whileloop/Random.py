import random

print("what is my magic number (1 to 100) ?")
mynumber = random.randint(1, 100)
print(mynumber)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) + ">>"
    if (ntries <= 6):
        yourguess = int(input(msg))
    if yourguess > mynumber:
        print("too high")
    else:
        print("too low")
    ntries += 1

if yourguess == mynumber:
    print("yes its", mynumber)
else:
    print("sorry my number is", mynumber)


