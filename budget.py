#creating a budget 
# remeber age = input("Your age: ")  # Comes in as string
# age = int(age)  # Convert to integer

#Housing rent 
months = float(input("Enter how many months a year do you pay for rent. Example every month(12), every 6 months(2)"))
spending = float(input("Enter your yearly spending for housing.:"))
housingyear = months * spending 
print(f"The yearly spending on housing is {housingyear:.2f}")

#Groceries 
times = float(input("Enter how many times a month you go grocerie shopping:"))
spending = float(input("Enter your average spending on groceries.:"))
grocerieyear = times * spending 
print( f"The yearly on groceries is {grocerieyear:.2f}")

#Transportation (truck) 
months = float(input("Enter how many times a month do you fill your gas tank")) 
spending = float(input("Enter the average spending when you fill up your gas tank"))
truckyear = months * spending 
print (f" The yearly cost of gas on empty is {truckyear:.2f}")

#Healthcare 
months = float(input("Enter how many months a year do you pay for healthcare. Example every month (12), every 6 months (2):"))
spending = float(input("Enter your yearly spending on healthcare:"))
healthcareyear = months * spending 
print(f"The yearly spending on healthcare is {healthcareyear:.2f}")

#Personal care 
spending =float(input("Enter on average how much a month do you spend on personal care: "))
personalcare = spending *12 
print(f"The average spending on persoanl care is {personalcare:.2f}")

#Debt 
balance = float(input("Enter the remaining balance of your debt: "))
intrest = float(input("Enter your intrest rate(in whole number):"))
totalintrest = balance * intrest
total = totalintrest + balance
length = float(inout("Enter the remaining time you have to pay on your loan (months):"))
debtyear = total/length
print(f"The yearly payment for your loan is {debtyear:.2f}")
