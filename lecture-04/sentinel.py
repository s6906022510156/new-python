keep_going = 'y'

while keep_going == 'y':
    whosales = float(input('Enter the item whosale cost: '))

    retailprice = whosales * 2.5
    print(f'The commission is ${retailprice:.2f}')

    keep_going = input('Do you want to calculate another' + 
                       ' commission (Enter y for yes): ')