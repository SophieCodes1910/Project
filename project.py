#Project part1 Sophie Mc Alavey R00243889
#Note - I realized after writing 106 lines of code that none of my git commits  had been pushed to the repository. Therefore, I had to create a new file on my laptop.

print("ONE DAY FILM FESTIVAL")
print("===" * 15)

def menu():
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
        name = input("Enter your name => ")
        booking_info.append(name)
        print("Choose the time slot")
        print("1: All Day")
        print("2: Morning")
        print("3: Afternoon")
        print("4: Evening")
        chosen_time = int(input(" => "))

        total_tickets = int(input("How many people in your group? => "))
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

        return name, booking_info , chosen_time, total_tickets, total_kids, total_popcorn
