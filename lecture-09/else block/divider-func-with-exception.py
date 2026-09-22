def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print("exception: ", e)
    else:
        return result

a,b = map(int,input("enter two number :").split())
print(divide(a,b))
print("end of program")