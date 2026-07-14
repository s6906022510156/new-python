hours = float(input("enter the number of hourse work : "))
HourlyPayRate = float(input("enter the hourly pa rate : "))
grosspay = hours * HourlyPayRate
if hours > 40:
    grosspay = (hours - 40) * HourlyPayRate * 1.5 +(40 * HourlyPayRate)
print("total pay for the week: $",grosspay)

