用python编写一个银行系统

# 创建银行类
class Bank():
    # 初始化
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    # 存钱
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"You deposited {amount}")
        return f"You deposited {amount}"

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"You withdrew {amount}")
        return f"You withdrew {amount}"

    # 查看余额
    def balance(self):
        return f"Your balance is {self.balance}"

    # 查看交易记录
    def show_transactions(self):
        return self.transactions