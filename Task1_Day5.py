import average_cal as ac

a_grd = open("Agrade.txt", "w+")
b_grd = open("Bgrade.txt", "w+")
c_grd = open("Cgrade.txt", "w+")


def sorted(r_no, name, res):
    if (res > 80) and (res <= 100):
        a_grd.write(r_no+"-"+name+"-"+str(res)+"\n")

    elif (res >= 60) and (res <= 80):
        b_grd.write(r_no+"-"+name+"-"+str(res)+"\n")

    else:
        c_grd.write(r_no+"-"+name+"-"+str(res)+"\n")


if __name__ == '__main__':
    no_of_stu = int(input("Enter no. of students"))
    rs = open("student_Info.txt", 'w+')
    mark = open("studentMarks.txt", "w+")
    for i in range(no_of_stu):
        r_no = input("Enter roll no. of student")
        naam = input("Enter name of student")
        rs.write(r_no+"-"+naam+"\n")
        mrk1 = input("Enter marks of science")
        mrk2 = input("Enter marks of maths")
        mrk3 = input("Enter marks of english")
        mark.write(r_no + "-" + mrk1 + "-" + mrk2 + "-" + mrk3 + "\n")
        res = ac.avrg(mrk1, mrk2, mrk3)
        sorted(r_no, naam, res)


# rs.seek(0, 0)
# lines = rs.read()
# print(lines)


# mark.seek(0, 0)
# lines = mark.read()
# print(lines)
