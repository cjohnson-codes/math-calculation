import math
#s Get user input

P0 = float(input("Enter the initial investment amount: "))
t = float(input("Enter the number of years: "))
r = float(input("Enter the annual interest rate (as a decimal): "))

# Calculate the final amount using continuous compounding

Pt = P0 * math.exp(r * t)

# Display the result
print("The value of the investment is:", Pt)