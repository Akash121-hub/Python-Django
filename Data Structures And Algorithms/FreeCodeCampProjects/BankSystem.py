from _typeshed import Self


class Account:
    def __init__(self,name,account_number,balance) -> None:
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}" + f"deposited {amount}" + f" and current balance is {self.balance}")

    def withdrwal(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name}" + f"withdrwal amount is {amount}" + f"and your current balace is {}")

    