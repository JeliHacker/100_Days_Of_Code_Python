#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
d = 2
print("{:.{}f}".format(23.4, d))

print(f"{d:.2f}")


# print("50{:2f}".format(2))
# print("Welcome to Eli's tip calculator!")

totalBill = float(input("What was the total bill? $"))
tipPercentage = float(input("How much tip would you like to give? (e.g 10, 12, 15, etc.) "))
people = int(input("How many people to split the bill? "))
totalCost = totalBill * (1 + (tipPercentage / 100))
eachPay = totalCost / people

print(f"Each person should pay: ${eachPay:.2f}")