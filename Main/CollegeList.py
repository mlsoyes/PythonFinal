# import person classes
from CollegeEmployee import CollegeEmployee
from Faculty import Faculty
from Student import Student

# lists to contain class instances
employees = []  # CollegeEmployee list
faculty = []  # Faculty list
students = []  # Student list


# function for displaying the data in the lists
def showListData(personList):  # takes a list as input and iterates through each object to display its data
    if len(personList) == 0:  # displays message if no data was entered
        print('No Data Entered')
        return
    for person in personList:
        person.showData()



# main loop
while 1:
    # ask user for data type
    match input('Enter data for college employee (C), faculty (F), or student (S)? (Enter Q to quit): \n').strip().upper():
        case "C":  # execute if user selects college employee
            if len(employees) < 4:  # ensures user cannot enter data for more than 4 CollegeEmployee instances
                employees.append(CollegeEmployee())  # creates a new CollegeEmployee and appends to the list of employees
                employees[len(employees)-1].setData()  # runs the set data function on the new instance
            else:  # print error if maximum has been reached
                print("Error: Maximum of 4 college employees reached")
                continue  # restart loop

        case "F":  # execute if user selects faculty
            if len(faculty) < 3:
                faculty.append(Faculty())  # creates new Faculty instance and appends to the list of faculty members
                faculty[len(faculty)-1].setData()  # runs the set data function on the new instance
            else:
                print("Error: Maximum of 3 faculty members reached")
                continue

        case "S":  # execute if user selects student
            if len(students) < 7:
                students.append(Student())
                students[len(students)-1].setData()
            else:
                print("Error: Maximum of 7 students reached")
                continue

        case "Q":
            break  # exit main loop to execute display functions

        case _:  # default case to catch invalid input
            print("Error: invalid input")
            continue


# display data and exit program
print("--Data Report-- \n")
# College Employee category
print("College Employees:")  # header
showListData(employees)  # data
# Faculty category
print("\nFaculty:")
showListData(faculty)
# Student category
print("\nStudents:")
showListData(students)

print("\n--end of report--")

