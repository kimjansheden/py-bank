class Customer:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.accounts = []
        self.__logged_in = False

    def remove(self, bank):
        self.logout(bank)
        self.username = None
        self.password = None
        self.accounts.clear()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def logged_in(self):
        return self.__logged_in

    def login(self, bank, username, password):
        if self.__helper_check_password(username, password):
            self.__logged_in = True
            if bank.logged_in_customer != {}:
                old_logged_in_customer: Customer = bank.get_customer(bank.logged_in_customer["logged_in_customer"],
                                                                     return_customer=True)
                if old_logged_in_customer.username == self.username:
                    print("You are already logged in.")
                    return
                old_logged_in_customer.__logged_in = False
            bank.logged_in_customer["logged_in_customer"] = self.username
            print("Login successful.")
        else:
            print("Wrong password.")

    def logout(self, bank, send_message=False):
        if not self.__logged_in:
            success = False
        else:
            success = True
            self.__logged_in = False
            bank.logged_in_customer.popitem()
        if send_message:
            if success:
                print("Logout successful")
            else:
                print("Logout failed. You are not logged in.")

    def add_account(self):
        from Account import Account
        Account(self)
        print("New account added.")

    def show_all_accounts(self):
        for account in self.accounts:
            print(account)

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username}"

    def __helper_check_password(self, username, password):
        if self.username == username and self.password == password:
            return True
