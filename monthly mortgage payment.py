# Calculate monthly mortgage payment

P0 = float(input("Enter the amount to finance: "))
r = float(input("Enter the annual interest rate (decimal form): "))
N = int(input("Enter the loan term in years: "))

k = 12  # monthly compounding

d = P0 / ((1 - (1 + r / k) ** (-N * k)) / (r / k))

print("Monthly payment:", d)