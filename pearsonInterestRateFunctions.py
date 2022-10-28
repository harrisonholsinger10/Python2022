# Compound Interest Rate Function

f = 0
p = float(input("Enter current bank balance:"))
i = float(input("Enter interest rate:"))
t = float(input("Enter the amount of time that passes:"))
    
    
def compoundInterest(p, i, t):
    
    f = p * (1 + i)**t
    print(f)

compoundInterest(p, i, t)