class UserAccount:
    bank_name = 'PKO'
    __operations_count = 6

    def __init__(self, name, card_number, cvv, date, balance):
        self.name = name
        self._card_number = card_number
        self._cvv = cvv
        self._date = date
        self.__balance = balance

    def put_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully added {amount} to your account.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw_money(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount} from your account.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance. Balance cannot be negative.")

    def get_balance(self):
        return self.__balance

    @classmethod
    def print_bank_name(cls):
        print (f'The bank name is {cls.bank_name}')


    @staticmethod
    def get_operations_count():
        return UserAccount.__operations_count

# Example usage
my_user_account = UserAccount("John Din", "1234 5678 9012 3456", "123", "01/24", 1000)

print("Initial Balance:", my_user_account.get_balance())
my_user_account.put_money(500)
print("Balance after deposit:", my_user_account.get_balance())
print('*' * 30)
my_user_account.withdraw_money(200)
print("Balance after withdrawal:", my_user_account.get_balance())
print('*' * 30)
UserAccount.print_bank_name()
print(f"Number of operations is: {UserAccount.get_operations_count()}")
