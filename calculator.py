class InterestCalculator:

    def __init__(self):
        self.type = ""
        self.interest_rate = 0
        self.deposit = 0
        self.goal = 0

    def set_goal(self, goal):
        self.goal = abs(goal)

    def set_monthly_deposit(self, deposit):
        self.deposit = abs(deposit)

    def set_interest_rate(self, rate):
        self.interest_rate = abs(float(rate / 1200))

    def set_type(self, type):
        self.type = type

    # .replace('$-', '-$')) note to future self
    def calculate_returns(self):
        month = 0
        total = 0
        done = False
        while abs(self.goal) > abs(total):
            month += 1
            if month == 1:
                total = self.deposit
            else:
                total += float(self.deposit + (total * self.interest_rate))
            self.savings_or_payment("Month {:d}: You have {:s} ${:0,.2f}", month, total, done)
        done = True
        self.savings_or_payment("It will take {:d} months to {:s} ${:0,.2f}", month, total, done)

    def savings_or_payment(self, string, month, total, boolean):
        if self.type.__contains__("sav") and not boolean:
            print(string.format(month, "saved", total))
        elif not self.type.__contains__("sav") and not boolean:
            print(string.format(month, "paid", total))

        if self.type.__contains__("sav") and boolean:
            print(string.format(month, "save", self.goal))
        elif not self.type.__contains__("sav") and boolean:
            print(string.format(month, "pay", self.goal))
