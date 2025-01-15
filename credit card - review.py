from dataclasses import dataclass

@dataclass
class CreditCard:
    card_name: str = ""
    card_limit: int = 0
    card_balance: float = 0.0
    card_transactions = []
    ID: str = "00001"

    def get_ID(self) -> str:
        return self.ID

    def get_card_name(self) -> str:
        return self.card_name

    def get_card_balance(self) -> float:
        return self.card_balance

    def set_card_name(self, name: str):
        assert type(name) == str, "Please enter a valid name string"
        self.card_name = name

    def set_card_limit(self, amount: int):
        assert type(amount) == int, "Please set card limit to integer value"
        self.card_limit = amount

    def add_card_transactions(self, amount: float):
        assert type(amount) == float, "Please set transaction to decimal value"
        if self.card_balance + amount > self.card_limit:
            print("Insufficient credit")
        else:
            self.card_transactions.append(amount)
            self.card_balance += amount

    def __str__(self):
        return f"{self.card_name}: current balance: ${self.card_balance:.2f}, credit limit: ${self.card_limit}"

def main():
    #creating CreditCard
    my_credit_card = CreditCard()

    #card details using setters
    my_credit_card.set_card_name("Yang Song Credit Card")
    my_credit_card.set_card_limit(5000)

    #+ transactions
    my_credit_card.add_card_transactions(200.75)
    my_credit_card.add_card_transactions(350.25)

    #call getters + print
    print(f"Card ID: {my_credit_card.get_ID()}")
    print(f"Card Name: {my_credit_card.get_card_name()}")
    print(f"Card Balance: ${my_credit_card.get_card_balance():.2f}")

    # Print the object using __str__ method
    print(my_credit_card)

if __name__ == "__main__":
    main()
