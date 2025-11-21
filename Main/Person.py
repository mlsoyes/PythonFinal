class Person:

    # initialization
    def __init__(self):
        # initialization of required variables. set to empty string for assigning values later
        self.firstName = ''  # first name
        self.lastName = ''  # last name
        self.address = ''  # address
        self.zip = ''  # zip code
        self.phoneNumber = ''  # phone number

    # set data function. assigns all variables using a series of inputs as specified by project requirements.
    def setData(self):
        self.firstName = input("Enter first name: ")
        self.lastName = input('Enter last name: ')
        self.address = input('Enter address: ')
        self.zip = input('Enter zip code: ')
        self.phoneNumber = input('Enter phone number: ')

    # display data function. Prints data in one line as specified by project requirements.
    def showData(self):
        print(self.getData())

    # get data function. returns a string with all the data on one line. Included to improve modularity of the class
    def getData(self):
        return f'First name: {self.firstName}, Last name: {self.lastName}, address: {self.address}, Zip code: {self.zip}, Phone number: {self.phoneNumber}'