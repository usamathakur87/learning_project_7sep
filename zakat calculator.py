# Function to calculate zakat based on user's input of assets
def calculate_zakat():
    # Get the amount of cash the user has in hand
    cash_in_hand = float(input("Enter cash in hand: "))
    
    # Get the amount of cash the user has in the bank
    cash_in_bank = float(input("Enter cash in bank: "))
    
    # Get the total amount of gold the user owns (in grams)
    gold_in_hand = float(input("Enter the amount of gold in grams: "))
    
    # Get the current price of gold per gram (user input or fetched from a source)
    gold_price_per_gram = float(input("Enter the current gold price per gram: "))
    
    # Calculate the total value of gold owned by the user
    gold_value = gold_in_hand * gold_price_per_gram
    
    # Calculate the total savings (cash in hand + cash in bank + value of gold)
    total_savings = cash_in_hand + cash_in_bank + gold_value
    
    # Calculate the Nisab (threshold) based on 7.5 tola of gold (87.48 grams)
    # If total savings exceed this value, Zakat is obligatory
    nisab = 87.48 * gold_price_per_gram
    
    # Print the total savings and the Nisab threshold for the user to see
    print(f"\nTotal Savings: {total_savings}")
    print(f"Zakat Nisab (Threshold based on 7.5 tola gold): {nisab}")
    
    # Check if the total savings are greater than or equal to the Nisab threshold
    if total_savings >= nisab:
        # If eligible, calculate zakat as 2.5% of the total savings
        zakat = total_savings * 0.025
        print(f"\nYou are eligible to pay Zakat.")
        print(f"Zakat to be paid: {zakat}")
    else:
        # If not eligible, inform the user that they are below the Nisab threshold
        print("\nYou are not eligible to pay Zakat as your savings are below the Nisab threshold.")

# Entry point of the program
if __name__ == "__main__":
    # Print a welcome message for the Zakat calculator
    print("===== Zakat Calculator =====")
    
    # Call the zakat calculation function
    calculate_zakat()

