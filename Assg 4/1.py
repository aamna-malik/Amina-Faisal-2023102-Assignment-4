class BankAccount:
    def __init__(self, account_number, balance, owner_name, pin):
        self._account_number = account_number  # Public attribute
        self._balance = balance  # Public attribute
        self.__owner_name = owner_name  # Private attribute
        self.__pin = pin  # Private attribute

    # Getter method for owner_name
    def get_owner_name(self):
        return self.__owner_name

    # Setter method for owner_name with validation
    def set_owner_name(self, new_owner_name):
        if isinstance(new_owner_name, str):
            self.__owner_name = new_owner_name
        else:
            print("Invalid owner name. Please provide a valid string.")

    # Getter method for pin
    def get_pin(self):
        return "****"  # For security reasons, only return a masked version

    # Setter method for pin with validation
    def set_pin(self, new_pin):
        if isinstance(new_pin, int) and len(str(new_pin)) == 4:
            self.__pin = new_pin
        else:
            print("Invalid PIN. Please provide a valid 4-digit PIN.")

# Example usage
account = BankAccount(account_number="123456789", balance=1000.0, owner_name="John Doe", pin=1234)

# Accessing public attributes
print("Account Number:", account._account_number)
print("Balance:", account._balance)

# Accessing private attributes using getter methods
print("Owner Name:", account.get_owner_name())
print("PIN:", account.get_pin())

# Modifying private attributes using setter methods
account.set_owner_name("Jane Doe")
account.set_pin(5678)

# Displaying updated information
print("Updated Owner Name:", account.get_owner_name())
print("Updated PIN:", account.get_pin())
