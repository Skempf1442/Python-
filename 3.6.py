#list of seats
available_seats = {1, 2 ,3 ,4 ,5 ,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

while True:
    print("\mnSeats:", available_seats)

    seat_choice = input("\n Enter what seat you would like")

    seat_choice = int(seat_choice)

    if seat_choice==0:
        print("\n Thank you!")
        break

    if seat_choice in available_seats:
        available_seats.remove(seat_choice)
        print(f"Seat {seat_choice} has been bought")
    else:
        print("Seat has been sold already.")
    if len(available_seats) ==0:
        print("\nSold out")
        break