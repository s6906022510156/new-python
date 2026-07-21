column = int(input("enter number of column"))
for i in range(1,101):
    print(f"{i:>5}" , end=" ")
    if i % column == 0:
        print()
    
