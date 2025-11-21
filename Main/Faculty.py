from Main.CollegeEmployee import CollegeEmployee
class Faculty(CollegeEmployee):

    #initialization
    def __init__(self):
        # call parent constructor
        super().__init__()
        # initialize isTenured boolean as false
        self.isTenured = False  # Boolean indicating whether the Faculty member is tenured

    # set data function. extends parent method
    def setData(self):
        # call to parent method
        super().setData()
        # while loop to ensure valid data is entered for isTenured value
        while 1:
            inp = input('Is this person tenured? (y/n): ').lower()  # local variable for user input. makes input lowercase
            if inp == 'y' or inp == 'yes':  # set isTenured to true if input is yes
                self.isTenured = True
                break  # exit loop if input is valid
            elif inp == 'n' or inp == 'no':  # set isTenured to false if input is no
                self.isTenured = False
                break  # exit loop if input is valid
            else:  # print error message and continue loop if input is invalid
                print(f'Error: Invalid input: \'{inp}\'')
                continue

    # get data function. overrides parent method
    def getData(self):
        # overridden return statement to append new data to inherited data
        return f'{super().getData()}, Tenured: {self.isTenured}'

    # it is still not necessary to override showData, as the method will still call the overridden getData function
