class BankAccount:
    """Класс для управления банковским счетом клиента."""

    def __init__(self, account_holder, balance=0):
        """
        Инициализация банковского счета.

        :param account_holder: Имя владельца счета
        :param balance: Начальный баланс (по умолчанию 0)
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Внести деньги на счет.

        :param amount: Сумма для внесения
        """
        if amount > 0:
            self.balance += amount
            print(f"На счет {self.account_holder} внесено {amount} единиц. Баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        """
        Снять деньги со счета.

        :param amount: Сумма для снятия
        """
        if amount > self.balance:
            print("Недостаточно средств для снятия.")
        elif amount > 0:
            self.balance -= amount
            print(f"Со счета {self.account_holder} снято {amount} единиц. Баланс: {self.balance}")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        """Вывести текущий баланс."""
        print(f"Баланс счета {self.account_holder}: {self.balance}")

# Пример использования класса
if __name__ == "__main__":
    account = BankAccount("Иван Иванов", 500)
    account.get_balance()
    account.deposit(200)
    account.withdraw(100)
    account.withdraw(700)
