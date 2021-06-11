demo = open("demo.txt", "w+")
dummy = open("dummy.txt", "w+")

n = int(input("Enter the number of lines"))


def writeDta(n_line):
    for i in range(n):
        con = input("Enter content of file")
        demo.write(con+"\n")


def readData(demo):
    demo.seek(0)
    cont = demo.read()
    print(cont)


def reverseData(demo):
    lst = []
    demo.seek(0, 0)
    for lines in demo:
        lst.append(lines)
    lst.reverse()
    dummy.writelines(lst)
    dummy.seek(0, 0)
    rev_line = dummy.read()
    print(rev_line)


def replace_data():
    fnd = input("Enter the word to be replaced")
    rplace = input("Enter the word to be replaced with")
    dummy.seek(0, 0)
    dt = dummy.read()
    dummy.close()
    dummy_data = open("dummy.txt", "w+")
    replaced_data = dt.replace(fnd, rplace)
    dummy_data.write(replaced_data)
    dummy_data.seek(0, 0)
    new_lines = dummy_data.read()
    print(new_lines)
    dummy_data.close()


writeDta(n)
readData(demo)
reverseData(demo)
replace_data()
