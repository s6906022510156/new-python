with open("sales.txt", "r") as sales_file:
    lines = sales_file.readlines()
    while line != "":
        amount = float(line)
        print(format(amount, ".2f"))
        line = sales_file.readline()