def get_amount():
    """Get the amount from user input"""
    while True:
        try:
            amount_to_convert = float(input("Enter the amount: "))
            if amount_to_convert <= 0:
                raise ValueError
            return amount_to_convert
        except ValueError:
            print("Invalid amount")


def get_currency(label):
    """Get currency (either Source or Target)"""
    currencies = ("EUR", "GBP", "BTC")
    while True:
        currency = input(
            f"{label} currency (EUR/GBP/BTC): ").strip().upper()
        if currency not in currencies:
            print("Invalid currency")
        else:
            return currency


def convert(amount_to_convert, source_currency, target_currency):
    """Convert an amount in a source currency to a target currency"""
    exchange_rates = {
        "GBP": {"EUR": 1.15937, "BTC": 0.000011260},
        "EUR": {"GBP": 0.862514, "BTC": 0.000009734953437},
        "BTC": {"EUR": 102.948, "GBP": 88.671468}
    }
    if source_currency == target_currency:
        return amount_to_convert

    return round(
        (amount_to_convert * exchange_rates[source_currency][target_currency]), 2)


def main():
    amount_to_convert = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    converted_amount = convert(
        amount_to_convert, source_currency, target_currency)

    print(
        f'{amount_to_convert} {source_currency} is equal to {converted_amount} {target_currency}')


if __name__ == "__main__":
    # Code exécuté uniquement si on lance ce fichier directement
    main()
