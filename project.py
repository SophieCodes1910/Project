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