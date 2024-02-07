class bankaccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep):
        self.balance+=dep
        print("Success!", dep, "Tenge has succesfully deposited on your bank account.")
        print("Your current balance is: ", self.balance)

    def withdraw(self, wdraw):
        if wdraw > self.balance:
            print("Sorry, you don`t have enough money on your balance")
        else:
            self.balance-=wdraw
            print("Success!", wdraw, "Tenge has succesfully withdrawed from your bank account.")
            print("Your current balance is: ", self.balance)

butt = bankaccount(input("Owner is: "), 0)
butt.deposit(int(input("Write a sum to deposit: ")))
butt.withdraw(int(input("Write a sum to withdraw: ")))