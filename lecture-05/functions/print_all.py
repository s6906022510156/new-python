def print_all(*args):
    for index, arg in enumerate(args):
        print(f"argument {index + 1}:{arg}")

print_all("python",3.8,True,[1,2,3],{"key":"value"})