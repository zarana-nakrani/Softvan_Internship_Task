import random

class BankInfo:
    def __init__(self, fn, ln, gender, addr):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = addr


class BankAccount:
    def __init__(self, acc_num, amount, p1):
        self.acno = acc_num
        self.amount = amount
        self.bankinfo = p1

class SavingAcc(BankAccount):
    minAmount = 10000
    rate_of_interest = 0.06
    simple_intrst = 0.0

    def interest(self, month):
        self.month = month
        year = self.month / 12
        self.simple_intrst = float((self.rate_of_interest * self.minAmount * year) / 100)


    def viewProfile(self):
        print("Firstname:", self.bankinfo.fn + "\n")
        print("Lastname:", self.bankinfo.ln + "\n")
        print("Gender:", self.bankinfo.gender + "\n")
        print("Address:", self.bankinfo.address + "\n")
        print("Account number:", self.acno, "\n")
        print("Amount:", self.amount, "\n")
        print("Rate:", self.rate_of_interest)
        print("Total interest:", self.simple_intrst)




class currentAcc(BankAccount):
    minAmount = 5000
    roi = 0

    def viewProfile(self):
        print("Firstname:", self.bankinfo.fn + "\n")
        print("Lastname:", self.bankinfo.ln + "\n")
        print("Gender:", self.bankinfo.gender + "\n")
        print("Address:", self.bankinfo.address + "\n")
        print("Account number:", self.acno, "\n")
        print("Amount:", self.amount, "\n")
        print("Rate:", self.roi)
        print("Total interest: There is no annual interest in current account")


class Main:
    def __init__(self):
        fn = input("Enter your first name")
        ln = input("Enter your last name")
        gender = input("Enter your gender")
        addr = input("Enter your city name")
        p1 = BankInfo(fn, ln, gender, addr)
        acc_num = random.randint(10 ** 12, (10 ** 13)-1)
        amount = int(input("Enter the amount for bank account"))
        # p2 = BankAccount(acc_num, amount, p1)
        acc_type = input("Enter the type of account: Saving/Current?")
        if acc_type == "saving":
            for i in range(3):
                if amount < 10000:
                    amount = int(input("Enter amount more than 10000"))
                    if i == 2:
                        exit()
                else:
                    month = int(input("Enter no of months"))
                    saving = SavingAcc(acc_num, amount, p1)
                    saving.interest(month)
                    saving.viewProfile()
                    break

        else:
            for i in range(3):
                if amount < 5000:
                    amount = int(input("Enter amount more than 5000"))
                    if i == 2:
                        exit()
                else:
                    print("You have successfully created Current account"+"\n"+"There is no interest for this type of account")
                    current = currentAcc(acc_num, amount, p1)
                    current.viewProfile()


obj = Main()