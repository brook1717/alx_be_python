class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated balance attribute (with underscore to indicate internal use)
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current balance: ${self._account_balance:.2f}")
