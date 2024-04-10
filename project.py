#Project part1 Sophie Mc Alavey R00243889
#Note - I realized after writing 106 lines of code that none of my git commits  had been pushed to the repository. Therefore, I had to create a new file on my laptop.

print("ONE DAY FILM FESTIVAL")
print("===" * 15)
def menu():
    print("1: Make a booking")
    print("2: Show Availability")
    print("3: Exit")
    menu_output = int(input("==> "))
    return menu_output 

def making_a_booking(menu_output):
    if menu_output == 1:
        booking_info = []
        print("BOOKING")
        print("===" * 15)
        while True:
            name = input("Enter your name => ")
            if len(name) < 3: # validation for if name is less than 3 characters
                print("Name must be more than 3 characters long.")
            elif len(name) > 10: # validation for if name is more than 10 characters
                print("Name cannot be longer than 10 characters.")
            else:
                booking_info.append(name)
                break
        print("Choose the time slot")
        print("1: All Day")
        print("2: Morning")
        print("3: Afternoon")
        print("4: Evening")
        chosen_time = int(input(" => "))

        total_tickets = int(input("How many people in your group? => ")) #Amended to calculate total - kids = adults
        booking_info.append(total_tickets)
        total_kids = int(input("How many kids in your group? => "))
        if total_kids <= total_tickets:
            booking_info.append(total_kids)
        else:
            print("Error: the number of kids is greater than the number of tickets - please select more tickets.")

        popcorn = input("Would you like to include popcorn on arrive Y/N: => ").lower()
        if popcorn == "y":
            total_popcorn = int(input("How many portions are required? =>"))
            booking_info.append(total_popcorn)
        else:
            total_popcorn = 0

        return name, booking_info , chosen_time, total_tickets, total_kids, total_popcorn

def booking_records(chosen_time, booking_info, total_tickets):
    max_tickets = {}
    with open("BookingNumbers.txt", "r") as data_file:
        for line in data_file:
            line_data = line.split(",")
            max_tickets[line_data[0]] = int(line_data[1])

        if chosen_time == 1: 
            if total_tickets <= max_tickets["AllDayTicket"]:
                max_tickets["AllDayTicket"] -= total_tickets
                with open("Allday.txt", "w") as output_file:
                    for data in booking_info:
                        print(data, file=output_file)
        
        if chosen_time == 2: 
            if total_tickets <= max_tickets["Morning"]:
                max_tickets["Morning"] -= total_tickets
                with open("Morning.txt", "w") as output_file:
                    for data in booking_info:
                        print(data, file=output_file)
        if chosen_time == 3: 
            if total_tickets <= max_tickets["Afternoon"]:
                max_tickets["Afternoon"] -= total_tickets
                with open("Afternoon.txt", "w") as output_file:
                    for data in booking_info:
                        print(data, file=output_file)
        if chosen_time == 4: 
            if total_tickets <= max_tickets["Evening"]:
                max_tickets["Evening"] -= total_tickets
                with open("Evening.txt", "w") as output_file:
                    for data in booking_info:
                        print(data, file=output_file)

def calculate_cost(chosen_time, total_tickets, total_kids, total_popcorn):
    cost = {}
    with open("costs.txt", "r") as data_file:
        for line in data_file:
            line_data = line.split(",")
            cost[line_data[0]] = float(line_data[1])
        if chosen_time == 1:
            ticket_cost = cost["day"] * total_tickets
            popcorn_cost = cost["popcorn"] * total_popcorn
            total_cost = ticket_cost + popcorn_cost
        else:
            ticket_cost = cost["film"] * total_tickets
            popcorn_cost = cost["popcorn"] * total_popcorn
            total_cost = ticket_cost + popcorn_cost
        
    return total_cost

def booking_details(name, total_tickets, total_popcorn, total_cost):
    while True:

        print("Booking Details")
        print("===" * 15)
        print(f"Name: {name}")
        print(f"Number of Tickets: {total_tickets}")
        print(f"Popcorn: {total_popcorn}")
        print(f"Total Cost: €{total_cost}.2f")
        input("Press Return to Continue: ")
        menu_output = menu() # returns user to menu once finished showing availability and they press return
        if  menu_output != '1':
            break

def show_availability():
    while True:
        print("ONE DAY FILM FESTIVAL - AVAILABILITY")
        print("===" * 15)
        with open("BookingNumbers.txt", "r") as data_file:
            for line in data_file:
                line = line.split(",")
                time_slot,available_seats,tickets_booked,kids_ticket = line.split(",")
                available_seats = int(available_seats)
                if available_seats > 0:
                    print(f"{time_slot} - Available Seats: {available_seats}")
                else:
                    print(f"{time_slot}: Booked Out")
        input("Press Return to Continue: ")
        menu_output = menu() # returns user to menu once finished showing availability and they press return
        if  menu_output != '2':
            break

def update_booking_numbers(available_seats): # amended to simplify and debug
    time_slot = {}
    total_seats = {}
    total_kids = {}
    for filename in ["Allday.txt", "Morning.txt", "Afternoon.txt", "Evening.txt"]:
        with open(filename, "r") as file:
            for line in file: 
                line = line.strip
                line = line.split(",")
                time_slot[line[0]] = line[0]
                total_seats[line[0]] = line[1]
                total_kids[line[0]] = line[2]
        
        with open("BookingNumbers.txt", "w") as file:
            time_slot[line[0]] = line[0]
            remaining_seats[line[0]] =remaining_seats[line[1]]
            total_seats[line[0]] = total_seats[line[2]]
            total_kids[line[0]] = total_kids[line[1]]
            for time_slot in file:
                remaining_seats = available_seats - total_seats

            file.write(f"{time_slot}, {remaining_seats},{total_seats}, {total_kids}\n")

def calulate_income():
    total_tickets = {}
    time = {}
    cost = {}
    with open("BookingNumbers.txt" "r") as data_file:
        for line in data_file:
            line_data = line.split(",")
            time[line_data[0]] = (line_data[0])
            total_tickets[line_data[0]] = int(line_data[1])

    with open("costs.txt", "r") as cost_data:
        for line in cost_data:
            cost_data = line.split(",")
            time[cost_data[0]] = (cost_data[0])
            cost[cost_data[0]] = float(cost_data[1])

            total_income = sum(cost)

    
    


    


    


def main(): # was calling the defs as I wrote the program to ensure it functioned correctly but added the main at the end for organisational purposes
    menu_output =menu()
    if menu_output == 1:
        booking_result = making_a_booking(menu_output)
        if booking_result is not None:
            name, booking_info, chosen_time, total_tickets,total_kids, total_popcorn = booking_result
            booking_records(chosen_time, booking_info, total_tickets)
            total_cost = calculate_cost(chosen_time, total_tickets, total_kids, total_popcorn)
            booking_details(name, total_tickets, total_popcorn, total_cost)
    elif menu_output == 2:
        show_availability()
    elif menu_output == 3:
        update_booking_numbers()
main()