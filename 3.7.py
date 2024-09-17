time_slots = ["Morning", "Miday", "Afternoon","Nighttime"]
heart_rate =[]
total_heart_rate = 0 
for slot in time_slots:
    heart_rate = int(input(f"Enter your heart rate (in BPM) in the {slot}:"))

    heart_rate.appened([slot, heart_rate])

    total_heart_rate + heart_rate
    
    avaerage_heart_rate = total_heart_rate / len(time_slots)

print(f"Average heart rate today: {avaerage_heart_rate:.2f} BPM")