def main():
    print("Welcome to the Finance Calculator!")

    # Prompt for user input
    try:
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your total monthly expenses: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Check for negative savings
    if monthly_savings < 0:
        print(f"You are spending more than you earn! Monthly deficit: ${-monthly_savings:.2f}")
    else:
        # Projected annual savings with 5% interest
        annual_savings = monthly_savings * 12
        interest = annual_savings * 0.05
        projected_savings = annual_savings + interest

        # Output results
        print(f"\nYour monthly savings: ${monthly_savings:.2f}")
        print(f"Projected savings after one year with 5% interest: ${projected_savings:.2f}")

if __name__ == "__main__":
    main()
