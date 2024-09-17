#Creating a list for days 
days = ["Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday"]

#Steps 
steps = []

#creating a loop, for 
for day in days:
    while True:
        num_steps = int(input(f"How many steps did you take on {days}"))
        if num_steps < 0: 
            print("Positive number only.")
        else:
            steps.append(num_steps)
            break 

for i in range(len(days)):
    print(f"you took {steps[i]} on {days[i]}")

total_steps = sum(steps)
print(f"\n The total number of steps: {total_steps}")

average= round(total_steps/len(steps))
print(f"\n The average number of steps: {average}")
