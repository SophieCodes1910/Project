#-------------------parameters & return values-------------------
def find_smallest_value(val1, val2):
    if val1 < val2:
        return val1
    else:
        return val2
    
def main():
    num1 = 4.5
    num2 = 14
    smallest_number = find_smallest_value(num1, num2)
    print(smallest_number)

main()

#-------------------returning more than one value-------------------
def get_student_info():
    name = input("Enter student number: ")
    class_code = input("What class are you in: ")
    return name, class_code

def main():
    name, class_code = get_student_info()
    print(f"{name} is in {class_code}")

main()
#-------------------validation functions-------------------
def get_string(prompt):
    while True:
        answer = input(prompt)
        length = len(answer)
        if length != 0:
            break
    return answer

#-------------------lists-------------------
list_of_numbers = [6,19,23,14]
#homogenous lists - list of all same types
ages = [5, 80, 66, 12]
#heterogeneous lists - list with different data types
info = ["Anne", 7, 104.2, "Cork"]
#mutable - any of the items in a list may be changes

#-------------------iterating over a list-------------------
flowers = ["Hydrangea", "Edelweiss", "Lavender"]
for name in flowers:
    print(name);
print("")
amount = len(flowers)
i = 0
while ( i < amount):
    print(f"{i + i}. {flowers[i]}")
    i = i+1
print(" ")
#-------------------Using enumerated list-------------------
for i, name in enumerate(flowers):
    print(f"{i+1}.  {name}")

#-------------------in operator for lists-------------------
racketSports = ["Tennis", "Badminton" , "Squash"]
list1 =["Basketball","Football","Rugby"]

if "tennis" in racketSports:
    print("Tennis is a racket sport")
if "tennis" not in list1:
    print("Not in list")

#-------------------Built in functions-------------------
grades_list =[45,77,58,65,72]
min_score = min(grades_list)
max_score = max(grades_list)
number_subjects = len(grades_list)
average_grade = (sum(grades_list))/number_subjects

#-------------------list slicing-------------------
sports = ["Soccer", "Rugby", "Hurling", "Tennis", "Cricket", "Badminton"]
racketSports = sports[3:6]
print(racketSports)

#-------------------List Methods-------------------
append(item) # adds item to end of a list
index(item) # returns the position of the item in a list
insert(index, item) #adds item at specified index
sort( ) # sorts the list in ascending order
remove(item) # removes the first occerence of the item
reverse()# reverses the order of items in the list
pop(position) # removes and returns an item from a given position in a list
count(item) # returns the number of occurences of a given item in a list
extend(new_list) #concatenates a new list with the list

#-------------------function to return an updated price list-------------------

def half_prices(list):
    new_prices = []
    for item in list:
        new_prices.append(item/2)
    return (new_prices)

def main():
    prices = [40.00, 30.50, 1.10, 99.00]
    print(prices)
    new_list = half_prices(prices)
    print(new_list)

#-------------------Strings as Lists-------------------
word1 = "Hawaii"
startLetters = word1[0:2]
endLetters = word1[-1]
print(word1[0])
#-------------------iterating over string-------------------
for x in word1:
    print(x)
pos = word1.index("w") #find position

#-------------------string specific operations-------------------
split # "Hello There" -> ["Hello", "There"]
join # ["Hello","There"] -> Hello There
find #finds a substring in a string
replace # replaces a substring with another string and returns a new string

#-------------------writing list to file-------------------
from random import randint

def create_list_random_number(number_of_numbers):
    return[randint(1,20) for i in range(number_of_numbers)]

def main():
    list_of_numbers = create_list_random_number[5]

    with open("my_file.txt", "w") as output_file:
        for numbers in list_of_numbers:
            print(numbers, file=output_file)

if __name__ == "__main__":
    main()

#-------------------reading strings from a file into list-------------------
def read_strings_from_file(filename):
    list_of_strings = []
    with open(filename) as data_file:
        for line in data_file:
            list_of_strings.append( line.strip())
    return list_of_strings
def main():
    names = read_strings_from_file("my_file.txt")
    print(names)

if __name__ == "__main__":
    main()

#-------------------reading integers from file to list-------------------
def read_integers_from_file(filename):
    list_of_integers = []
    with open(filename) as data_file:
        for line in data_file:
            list_of_integers.append( int(line))
    return list_of_integers

def main():
    numbers = read_integers_from_file("my_file.txt")
    print(numbers)
if __name__ == "__main__":
    main()

#reading multiple pieces of data on line (CSV) - records
def read_data(name_of_file):
    connection = open(name_of_file)
    names_list = []
    scores_list = []
    with open("judges.txt") as file_connection:
        for line in file_connection:
            line = line.rstrip()
            line_data = line.split(",")
            names_list.append(line_data[0])
            scores_list.append(int(line_data[1]))
    return names_list, scores_list
if __name__ == "__main__":
    filename = "judges.txt"
    names, ages = read_data(filename)
    print(names)
    print(ages)

#sample exam question

def get_teacher_and_class():
    teacher_name = input("teacher name?: ")
    class_group = int(input("Class group?: "))
    return teacher_name, class_group

def get_names_and_numbers():
    children_names = []
    number_of_books = []
    amount_of_children = int(input("How many kids in the class?: "))
    for i in range (amount_of_children):
        names = input("Enter child name: ")
        children_names.append(names)
        book_count = int(input("How many books?: "))
        number_of_books.append(book_count)
    return children_names, number_of_books

def show_results_over_three(children_names, number_of_books):
    for i in range(len(number_of_books)):
        if number_of_books[i] > 3:
            print(f"{children_names[i]} read {number_of_books[i]} books.")

def get_average(number_of_books):
    average = sum(number_of_books) / len(number_of_books)
    return average

def show_spread(number_of_books):
    count_more_than_three = sum(1 for books in number_of_books if books > 3)


def main():
    teacher_and_class = get_teacher_and_class()
    kids_and_books = get_names_and_numbers()
    print(teacher_and_class)
    print(kids_and_books)

if __name__ == "__main__":
    main()