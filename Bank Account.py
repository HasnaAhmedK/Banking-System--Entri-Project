class Bank:
    def __init__(self):
        self.account={}
        self.logged_in_account = None

    def create_account(self,account_no,name,initial_balance,password):
        if account_no in self.account:
            print("Account already exists")
        else:
            self.account[account_no]={
                "Name":name,
                "Balance":initial_balance,
                "password": password,}
            print("Account created succesfully for Account no:",account_no)

    def account_login(self,account_no):
            password=input("Enter PIN: ")

            if account_no in self.account and self.account[account_no]["password"]==password:
                self.logged_in_account=account_no
                print("Account",account_no,"is logged in succesfully")
            else:
                print("Incorrect account number or Password")

    def logout(self):
        self.logged_in_account=None
        print("Logged out succesfully")

    def is_logged_in(self):
        return self.logged_in_account is not None

    def deposit(self,account_no):
        deposit_amount=int(input("Enter deposit amount: "))
        if not self.is_logged_in():
            return "Please log in first."
        x=self.account[account_no]["Balance"]
        final_balance=x+deposit_amount
        self.account[account_no]["Balance"]=final_balance
        print(f"${deposit_amount} has been deposited to your Account with account number: {account_no}\nNew Balance amount {final_balance}")

    def withdraw(self,account_no,withdraw_amount):
        if not self.is_logged_in():
            return "Please log in first."

        x=self.account[account_no]["Balance"]
        if x<withdraw_amount:
            print("Insufficiant balance")
        else:
            final_balance=x-withdraw_amount
            self.account[account_no]["Balance"] = final_balance
            print(f"${withdraw_amount} has been debitted from your Account with account number: {account_no} \nNew Balance {final_balance}")

    def check_balance(self,account_no):
        Current_balance=self.account[account_no]["Balance"]
        print(f"Current balance: {Current_balance}")

b1=Bank()
b2=Bank()
b1.create_account(1234,"Eva",1000,"pass1234")
b2.create_account(5678,"John",2500,"pass5678")

b1.account_login(1234)
print(b1.deposit(1234))
b1.check_balance(1234)

print(b2.deposit(5678))






