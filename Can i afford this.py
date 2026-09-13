# Calculate the maximum loan amount for 15-year and 30-year mortgages

d = float(input("Enter the monthly payment you can afford: "))
r = float(input("Enter the annual interest rate (decimal form): "))

k = 12  # monthly compounding

P15 = d * ((1 - (1 + r / k) ** (-15 * k)) / (r / k))
P30 = d * ((1 - (1 + r / k) ** (-30 * k)) / (r / k))

print("Maximum loan for a 15-year mortgage:", P15)
print("Maximum loan for a 30-year mortgage:", P30)