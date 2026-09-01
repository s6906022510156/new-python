with open("example.txt", "r") as outfile:
    line = outfile.readline()
    while line:
        print(line.strip())#มีstrip() เพื่อเอา \n ออก
        print("-------------")
        print(line)#ไม่มีstrip() จะมี \n อยู่
        line = outfile.readline()