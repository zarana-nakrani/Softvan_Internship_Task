from Task1_Day5 import sorted


class StudentInfo:
    def __int__(self, r_no, naam):
        self.roll = r_no
        self.name = naam


class StudentMarks:
    def __init__(self, r_no, mrk1, mrk2, mrk3):
        self.roll = r_no
        self.m1 = mrk1
        self.m2 = mrk2
        self.m3 = mrk3

    some = 0

    def avrg(self):
        some = int(self.m1) + int(self.m2) + int(self.m3)
        avg = some // 3
        return avg


class Main:
    def __init__(self):
        n = int(input("Enter the no. of students"))
        for i in range(n):
            r_no = input("Enter roll no. of student: ")
            naam = input("Enter name of student: ")
            mrk1 = int(input("Enter marks of maths"))
            mrk2 = int(input("Enter marks of science"))
            mrk3 = int(input("Enter marks of english"))
            si = StudentInfo()
            sm = StudentMarks(r_no, mrk1, mrk2, mrk3)
            avg = sm.avrg()
            sorted(r_no, naam, avg)


obj = Main()

