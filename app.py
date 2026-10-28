class FinanceCalculator:
    """Калькулятор личных финансов."""

    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, amount):
        """Добавляет доход."""
        if amount <= 0:
            raise ValueError("Сумма дохода должна быть положительной")
        self.incomes.append(amount)

    def add_expense(self, amount):
        """Добавляет расход."""
        if amount <= 0:
            raise ValueError("Сумма расхода должна быть положительной")
        self.expenses.append(amount)

    def total_income(self):
        """Возвращает общую сумму доходов."""
        return sum(self.incomes)

    def total_expenses(self):
        """Возвращает общую сумму расходов."""
        return sum(self.expenses)

    def balance(self):
        """Рассчитывает остаток средств."""
        return self.total_income() - self.total_expenses()


def main():
    calculator = FinanceCalculator()

    while True:
        print("\n=== Калькулятор личных финансов v2 ===")
        print("1. Добавить доход")
        print("2. Добавить расход")
        print("3. Показать финансовый отчёт")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                amount = float(input("Введите сумму дохода: "))
                calculator.add_income(amount)
                print("Доход добавлен.")
            except ValueError as error:
                print(f"Ошибка: {error}")

        elif choice == "2":
            try:
                amount = float(input("Введите сумму расхода: "))
                calculator.add_expense(amount)
                print("Расход добавлен.")
            except ValueError as error:
                print(f"Ошибка: {error}")

        elif choice == "3":
            print(f"Доходы: {calculator.total_income():.2f} руб.")
            print(f"Расходы: {calculator.total_expenses():.2f} руб.")
            print(f"Баланс: {calculator.balance():.2f} руб.")

        elif choice == "0":
            print("Работа завершена.")
            break

        else:
            print("Неизвестная команда. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()