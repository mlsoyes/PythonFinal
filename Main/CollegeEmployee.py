from Main.Person import Person

class CollegeEmployee(Person):

    # initialization
    def __init__(self):
        # call to parent constructor
        super().__init__()
        # declaration of new variables
        self.ssn = ''  # social security number
        self.pay = 0.0  # annual salary
        self.dept = ''  # department name

    # set data function. extends parent method
    def setData(self):
        # call to parent method in order to define the base variables for the class
        super().setData()
        self.ssn = input('Enter social security number: ')
        # try loop to catch invalid input for salary
        while 1:
            try:
                self.pay = float(input('Enter annual salary: $'))
                break # exit loop if input is valid
            except ValueError as e: # catch error and prompt user for salary again
                print(f'Error: Invalid input: {str(e)[str(e).index(":")+2:]}  Please enter salary as a number. (Do not include \'$\')')  # str(e)[str(e).index(":")+2:] used to return the user input that was invalid
                continue
        self.dept = input('Enter the department name: ')

    # get data function. overrides parent method
    def getData(self):
        # overridden print statement to include new data.
        return f'{super().getData()}, Social security number: {self.ssn}, Annual salary: ${self.pay:.2f}, Department name: {self.dept}'  # super().getData() used to prepend the inherited data to the new data

    # override to showData is not required as it calls getData(), which has already been overridden to include the new information.
