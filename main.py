from calculator import InterestCalculator

calculator = InterestCalculator()
calculator.set_type(input("Savings or loan repayment? ").lower())
if calculator.type.__contains__("sav"):
    calculator.set_goal(int(input("Savings goal: ")))
    calculator.set_monthly_deposit(int(input("Monthly deposit: ")))
    calculator.set_interest_rate(int(input("Annual interest rate: ")))
else:
    calculator.set_goal(int(input("Loan amount: ")))
    calculator.set_monthly_deposit(int(input("Monthly payment: ")))
    calculator.set_interest_rate(int(input("Annual interest rate: ")))

calculator.calculate_returns()
