from Customer import Customer
from Account import Account
import json


class Bank:
    """The bank and its functions."""
    def __init__(self, repopulate_from=""):
        self.logged_in_customer = {}
        self.__customers_list = []
        self.__accounts_list = []
        # If value is passed in the repopulate_from variable, initialize the instance with data from the previous
        # instance. The previous instance is thus recreated.
        if repopulate_from != "":
            self.repopulate(repopulate_from)

    def get_customers(self):
        return self.__customers_list

    def accounts_list(self):
        return self.__accounts_list

    def show_all_accounts(self):
        for account in self.__accounts_list:
            print(account.account_number, account.owner, account.get_balance)

    def get_accounts(self, username: str = ""):
        """Returns all accounts of the user."""
        if username != "":
            return self.get_customer(username, return_accounts=True)
        if self.logged_in_customer != {}:
            return self.get_customer(self.logged_in_customer["logged_in_customer"], return_accounts=True)
        else:
            print("You need to be logged in or specify a user.")

    def get_account(self, account_number: int):
        if self.logged_in_customer != {}:
            account: Account = self.__helper_get_account_from_logged_in_customer(account_number)
            # If account does not exist or does not belong to this customer, account will be of NoneType.
            # Only proceed if account is not of NoneType.
            if account is not None:
                print(account.as_string())
            else:
                print(f"Could not get account {account_number}. No such account belongs to you.")
        else:
            print("You need to be logged in to do that.")

    def get_balance_of(self, account_number=0):
        if account_number != 0:
            return self.__helper_get_balance(account_number)
        return "Enter a valid account number"

    def deposit(self, account_number: int, amount: int):
        if self.logged_in_customer != {}:
            account = self.__helper_get_account_from_logged_in_customer(account_number)
            # If account does not exist or does not belong to this customer, account will be of NoneType.
            # Only proceed if account is not of NoneType.
            if account is not None:
                # Only proceed if the amount is greater than 0.
                if amount > 0:
                    Account.deposit(account, amount)
                    print(f"{amount} kr successfully deposited to account {account_number}.")
                else:
                    print("Amount needs to be greater than 0")
            else:
                print(f"Deposit to account {account_number} failed. No such account belongs to you.")
        else:
            print("You need to be logged in to do that.")

    def withdraw(self, account_number, amount):
        if self.logged_in_customer != {}:
            account: Account = self.__helper_get_account_from_logged_in_customer(account_number)
            # If account does not exist or does not belong to this customer, account will be of NoneType.
            # Only proceed if account is not of NoneType.
            if account is not None:
                # Only proceed if the amount is greater than 0.
                if amount > 0:
                    # Only proceed if the balance can cover the withdrawal.
                    if amount <= account.get_balance:
                        Account.withdraw(account, amount)
                        print(f"{amount} kr withdrawed successfully.")
                    else:
                        print(f"Withdrawal failed. Insufficient balance.")
                else:
                    print("Amount needs to be greater than 0")
            else:
                print(f"Withdrawal to account {account_number} failed. No such account belongs to you.")
        else:
            print("You need to be logged in to do that.")

    def change_owner_of(self, account_number: int, new_owner: str):
        customer: Customer = self.get_customer(new_owner, return_customer=True, send_message=False)
        success = False
        # If username does not exist, customer will be of NoneType.
        # Only proceed if customer is not of NoneType.
        if customer is not None:
            for account in self.__accounts_list:
                if account.account_number == account_number:
                    old_owner = account.owner
                    new_owner_customer = self.get_customer(new_owner, return_customer=True)
                    # If the old owner is the same as the new owner, do not proceed.
                    if old_owner == new_owner_customer:
                        print(f"Account {account_number} is already owned by {new_owner}.")
                        return
                    account.owner = new_owner_customer
                    print(f"Account {account_number} is now owned by {new_owner}.")
                    return
        else:
            print(f"{new_owner} is not a customer of this bank.")
        if not success:
            print(f"Account {account_number} does not exist in this bank.")

    def change_customer_password(self, name: str, new_password: str):
        for customer in self.__customers_list:
            if customer.username == name:
                customer.password = new_password
                print("Password changed successfully.")
                return True
            else:
                print("Could not change password.")
                return False

    def change_customer_username(self, name: str, new_name: str):
        customer: Customer = self.get_customer(name, return_customer=True, send_message=False)
        # If username does not exist, customer will be of NoneType.
        # Only proceed if customer is not of NoneType.
        if customer is not None:
            # Check if username is not already taken.
            if not self.get_customer(new_name, return_username_taken=True):
                customer.username = new_name
                print("Username changed successfully.")
            else:
                print("Failed to change username. Name is already taken.")
        else:
            print(f"Failed to change username. No customer with username {name} exists.")

    # Recreates the customers and the accounts of the bank instance that was saved at the end of the application.
    def repopulate(self, bank_json_file: str):
        with open(bank_json_file, "r") as f:
            bank_json = json.load(f)
        # Repopulates the customers in the bank.
        for customer in bank_json[0]:
            self.add_customer(name=customer["_Customer__username"], password=customer["_Customer__password"],
                              send_message=False)
        # Repopulates the accounts in the bank.
        for acc in bank_json[1]:
            new_account = Account(owner=self.get_customer(acc["_Account__account_owner"], return_customer=True,
                                                          send_message=False),
                                  repopulate_id=acc["_Account__account_number"], balance=acc["_Account__balance"])
            self.__accounts_list.append(new_account)
        Account.set_highest_id_from_json(bank_json_file)

    def add_customer(self, name, password, send_message=True):
        # Check if username is not already taken.
        if not self.get_customer(name, return_username_taken=True):
            new_customer = Customer(name, password)
            self.__customers_list.append(new_customer)
            if send_message:
                print("Customer successfully added.")
        else:
            if send_message:
                print(f"Failed to add account with username {name}. Name is already taken.")

    def remove_customer(self, name):
        customer: Customer = self.get_customer(name, return_customer=True)
        # If username does not exist, customer will be of NoneType.
        # Only proceed if customer is not of NoneType.
        if customer is not None:
            customer.remove(self)
            self.__customers_list.remove(customer)

    def add_account(self, username: str = ""):
        if username != "":
            customer: Customer = self.get_customer(username, return_customer=True)
            # If username does not exist, customer will be of NoneType.
            # Only proceed if customer is not of NoneType.
            if customer is not None:
                new_account = Account(self.get_customer(username, return_customer=True))
                self.__accounts_list.append(new_account)
                print("Account successfully added.")
                return
        if self.logged_in_customer != {}:
            new_account = Account(
                self.get_customer(self.logged_in_customer["logged_in_customer"], return_customer=True))
            self.__accounts_list.append(new_account)
            print("Account successfully added.")
            return
        else:
            print("You need to be logged in or specify a user.")

    def remove_account(self, account_number: int):
        if self.logged_in_customer != {}:
            account = self.__helper_get_account_from_logged_in_customer(account_number)
            # If account does not exist or does not belong to this customer, account will be of NoneType.
            # Only proceed if account is not of NoneType.
            if account is not None:
                Account.remove(account)
                self.__accounts_list.remove(account)
                print(f"Account {account_number} removed successfully.")
            else:
                print(f"Removal of account {account_number} failed. No such account belongs to you.")
        else:
            print("You need to be logged in to do that.")

    def login(self, username: str, password: str):
        customer = self.get_customer(username, return_customer=True)
        # If username does not exist, customer will be of NoneType.
        # Only proceed if customer is not of NoneType.
        if customer is not None:
            Customer.login(customer, self, username, password)

    def logout(self):
        if self.logged_in_customer != {}:
            customer = self.get_customer(self.logged_in_customer["logged_in_customer"], return_customer=True)
            # If username does not exist, customer will be of NoneType.
            # Only proceed if customer is not of NoneType.
            if customer is not None:
                Customer.logout(customer, self, send_message=True)
        else:
            print("You need to be logged in to do that.")

    def serialize(self):
        bank_customers = []
        for customer in self.__dict__['_Bank__customers_list']:
            bank_customers.append(customer.__dict__)
        bank_accounts = []
        for account in self.__dict__['_Bank__accounts_list']:
            bank_accounts.append(account.__dict__)
        highest_id = {"highest_id": Account.highest_id()}
        serialized_bank = [bank_customers, bank_accounts, highest_id]
        return serialized_bank

    # Helper function to find a customer from a username string and return various things depending on the parameters.
    def get_customer(self, username: str, return_customer=False, return_accounts=False, return_username_taken=False,
                     send_message=True):
        if return_customer:
            for customer in self.__customers_list:
                if customer.username == username:
                    return customer
            if send_message:
                print(f"No such username: {username}")

        if return_username_taken:
            for customer in self.__customers_list:
                if customer.username == username:
                    return True
            return False

        if return_accounts:
            for customer in self.__customers_list:
                if customer.username == username:
                    return f"{username}s konton: {customer.accounts}"
            return f"No such username: {username}"

    # Verify that an account belongs to a customer and return that account.
    def __helper_get_account_from_logged_in_customer(self, account_number):
        customer: Customer = self.get_customer(self.logged_in_customer["logged_in_customer"], return_customer=True)
        account_to_verify = self.__helper_get_account(account_number)
        # If the account does not exist: exit.
        if account_to_verify is None:
            return account_to_verify
        # Check if the customer owns the account. If true, return the account. Otherwise return None.
        for account_owned_by_customer in customer.accounts:
            if account_owned_by_customer == account_to_verify:
                return account_owned_by_customer

    def __helper_get_account(self, account_number):
        # Get account from account number.
        for account in self.__accounts_list:
            if account.account_number == account_number:
                return account

    def __helper_get_balance(self, account_number):
        for account in self.__accounts_list:
            if account.account_number == account_number:
                return account.__balance


bank = Bank()
