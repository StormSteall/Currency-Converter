# Predefined exchange rates (as of a specific date, for simplicity)
exchange_rates = {
    "USD": {"GBP": 0.74, "EUR": 0.85, "JPY": 110.50},
    "GBP": {"USD": 1.35, "EUR": 1.15, "JPY": 150.20},
    "EUR": {"USD": 1.18, "GBP": 0.87, "JPY": 130.70},
    "JPY": {"USD": 0.009, "GBP": 0.0067, "EUR": 0.0076}
}

def display_currencies():
    """Display available currencies."""
    print("Available currencies:")
    for currency in exchange_rates.keys():
        print(f"- {currency}")

def convert_currency():
    """Convert an amount from one currency to another."""
    # Display available currencies
    display_currencies()

    # Get user input
    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., GBP): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))

    # Check if currencies are valid
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        # Perform the conversion
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency pair. Please try again.")

def main():
    """Main program loop."""
    while True:
        print("\nCurrency Converter")
        print("1. Convert Currency")
        print("2. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            convert_currency()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
