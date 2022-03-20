class ATM:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    def CashWithdrawal(self):
        print("Cash Withdrawn")
    def BalanceEnquiry(self):
        print("Balance Enquired")

ATM = ATM("1234567890", "1234")
print(ATM.card_number)
print(ATM.pin_number)
ATM.CashWithdrawal()
ATM.BalanceEnquiry()