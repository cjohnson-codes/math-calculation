# Calculate the monthly deposit needed to reach a goal

target = float(input("Enter the desired down payment amount: "))
r = float(input("Enter the annual interest rate (decimal form): "))

k = 12  # monthly compounding

d = target / (((1 + r / k) ** 24 - 1) / (r / k))

print("Required monthly deposit:", d)