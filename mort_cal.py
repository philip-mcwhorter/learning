#fixed variables
## Fixed variables are mostly unliked, as we don't have good reasons typically to make these
## fixed vars. Usually, you want this passed in by a user or you want the application to read
## the variables from a config file, where they can be modified instead
interest_rate = 3.75
property_tax = 0.0167
numberPaymentsPerYear = 12
term = 30
totalMonths = numberPaymentsPerYear * term
escrow = int(1046.88-257.36)
principalPercent = .2
affordableMortgage = 1500
inputMessage = "Input New Home Price: "
successMessage = "Yay! You can afford this house!"
failureMessage = "Bummer. Try again."

def mortgage(principal):
    rate_adjust = interest_rate/1200
    rate_monthly = (1+rate_adjust)**totalMonths
    prin_form = (rate_adjust*rate_monthly)/(rate_monthly-1)
    mon_princ = principal*prin_form
    mon_payment = mon_princ + escrow
    return int(mon_payment)

def calculator():
    while True:
        x = int(input(inputMessage))
        principal = x - (x * principalPercent)   
        mortage_payment_month = mortgage(principal)
        if mortage_payment_month <= affordableMortgage:
            print(successMessage)
            break
        else:
            print(failureMessage)
            continue
            
            
calculator ()
