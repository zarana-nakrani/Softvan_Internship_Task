class HDFC:
    __max_amount = 20000
    max_transaction = 3

    def withdraw(self, amount):
        self.__max_amount = self.__max_amount - self.amount
        self.max_transaction -= 1



class Axis:
    __max_amount = 30000
    max_transaction = 5

    def withdraw(self, amount):
        self.__max_amount = self.__max_amount - self.amount


class Main:
    def __init__(self):
        choice = int(input("Your Bank: 1.HDFC or 2.Axis\n Enter 1 or 2"))
        amount = 0

        def inputAmount(self):
            self.amount = int(input("Enter the amount to be transferred"))
            hdfc = HDFC()
            axis = Axis()
            if choice == 1:
                if amount > 20000 or hdfc._HDFC__max_amount == 0:
                    print("Transaction amount must be less than 20000")
                    exit()
                elif hdfc.max_transaction == 0:
                    print("Max transaction limit exceeded")
                    exit()
                else:
                    hdfc.withdraw(amount)

            else:
                if amount > 30000 or axis._Axis__max_amount == 0:
                    print("Transaction amount must be less than 30000 or max amount for transaction exceeded")
                elif axis.max_transaction == 0:
                    print("Max transaction limit exceeded")
                else:
                    axis.withdraw(amount)


obj = Main()

