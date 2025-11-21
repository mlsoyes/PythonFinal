from Main.Person import Person
class Student(Person):

    # initialization
    def __init__(self):
        # call parent constructor
        super().__init__()
        # initialize new variables
        self.major = ''  # Major field of study
        self.gpa = 0.0  # Grade point average

    # set data function. Extends parent method
    def setData(self):
        # call to parent method
        super().setData()
        # try loop to catch invalid input for GPA
        while 1:
            try:
                self.gpa = float(input('Enter GPA: '))
                break  # exit loop if input is valid
            except ValueError as e:  # catch error and prompt user for salary again
                print(f'Error: Invalid input: {str(e)[str(e).index(":") + 2:]}  Please enter GPA as a number.')  # str(e)[str(e).index(":")+2:] used to return the user input that was invalid
                continue
        self.major = input('Enter Major field of study: ')

    # get data function. Overrides parent method
    def getData(self):
        return f'{super().getData()}, Major: {self.major}, GPA: {self.gpa}'

    # showData method override not required. Parent method calls the overridden getData function
