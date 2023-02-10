import json

from Customer import Customer


class Account:
    __id = 0

    @classmethod
    def highest_id(cls):
        return cls.__id

    # funktion som läser från json-filen vilket kontonr som är det högsta och sparar det till __id så räknaren kan
    # fortsätta därifrån.
    @classmethod
    def set_highest_id_from_json(cls, bank_json_file):
        with open(bank_json_file, "r") as f:
            bank_json = json.load(f)
        # Only change the highest id if the one on file is higher.
        if cls.__id < bank_json[2]['highest_id']:
            cls.__id = bank_json[2]['highest_id']

    def __init__(self, owner=None, repopulate_id=0, balance=0):
        if repopulate_id == 0:
            Account.__id += 1
            self.__account_number = Account.__id
        else:
            self.__account_number = repopulate_id
        self.__balance = balance
        self.__account_owner = owner

        if isinstance(owner, Customer):
            owner.accounts.append(self)

    def remove(self):
        self.__account_owner.accounts.remove(self)
        self.__account_owner = None

    @property
    def get_balance(self, account_number=0):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    @property
    def account_number(self):
        return self.__account_number

    @property
    def owner(self):
        return self.__account_owner

    @owner.setter
    def owner(self, new_owner):
        old_owner = self.__account_owner
        if isinstance(old_owner, Customer) and old_owner != new_owner:
            old_owner.accounts.remove(self)
        if isinstance(old_owner, Customer) and old_owner == new_owner:
            return
        new_owner.accounts.append(self)
        self.__account_owner = new_owner

    def __str__(self):
        return f"'account_number':{self.account_number}:'balance':{self.get_balance}:'owner':{self.owner}"

    def as_string(self):
        return f"{self.owner} äger konto {self.account_number} och har {self.get_balance} kr på sitt konto."

    def __repr__(self):
        return f"{self.account_number}"
