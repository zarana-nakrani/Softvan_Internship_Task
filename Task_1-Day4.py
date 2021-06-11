filename = input("Enter the name of file")
n = int(input("Enter the no. of lines"))
obj = open(filename, "w+")


def writeData():
    for i in range(n):
        x = input("Enter the content of file")
        obj.write(x+"\n")


def readData():
    obj.seek(0)
    lines = obj.read()
    print(lines)


def countData():
    obj.seek(0)
    str_data = []
    line_no = 0
    word = 0
    words_with_space = 0
    for lines in obj:
        str_data.append(lines.split(" "))
        line_no += 1
    print("line number=", line_no)
    for i in range(len(str_data)):
        word += len(str_data[i])
    print("words without space=", word)
    obj.seek(0)
    strg = obj.read()
    for i in strg:
        if i == " ":
            words_with_space += 1
    words_with_space += word
    print(words_with_space)
    obj.close()


writeData()
readData()
countData()
obj.close()