## Inouts we need from the user
# total rent
# total food ordered
# electricirty units spent
# charge per unit
# number of person living 

#output
# Total amount 
# total amount to be paid by each person


rent =  float(input("Enter the total rent: "))
food = float(input("Enter the amount of money spent in food: "))
electricity = float(input("Enter the amount of electricity units: "))
electcharge = float(input("Enter the amount of charge per unit: "))
person = int(input("Enter the number of person living: "))

total = rent + food + (electricity * electcharge)
totalAmtpp = total / person

print("The total amount for this month is ", total)
print("The total amount to be paid by per person is ", totalAmtpp)