def example_w_plus_mode():
    with open("example_w_plus.txt", "w+") as file:
        file.write("this is a firsst line in the file\n")
        file.write("this is a second line in the file\n")

        file.seek(0)  # Move the cursor to the beginning of the file
        content = file.read()
        print("content of the file: ")
        print(content)

example_w_plus_mode()