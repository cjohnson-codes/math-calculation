# Calculate the final balance after 24 months

d = float(input("Enter the amount deposited each month: "))
r = float(input("Enter the annual interest rate (decimal form): "))

k = 12  # monthly compounding

P24 = d * (((1 + r / k) ** 24 - 1) / (r / k))

print("Final balance after 24 months:", P24)