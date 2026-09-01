num_days = int(input("for how many days do you have sales?"))
with open("sales.txt", "w") as sales_file:
    for count in range(1, num_days + 1):
        sales = float(input(f"enter the sales for day#{count}: "))
        sales_file.write(str(sales) + "\n")

print("data written to sales.txt")