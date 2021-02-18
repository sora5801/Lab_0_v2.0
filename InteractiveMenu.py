from Database import Database
import re

class UserInterface:
    def __init__(self):
        return None

    def printoutinfo(self, **kwargs):  # Used Kwargs here to display dictionary infos
        for i in kwargs.items():
            print(i)

    def InteractiveMenu(self):
        B = Database()
        B.ReadCarbonEmission()
        B.ReadTemperature()
        B.FillinCO2andTempdata()  # Create a default dict that contains both CO2 and Temperature tuples
        print('Welcome!\n')
        print('This is a program that allows you to select a year where the data from two files')
        print('overlap and compares the CO2 emission levels to the temperature for the selected year.\n')
        menu = {}
        menu['1'] = "Search Temperature data by year."
        menu['2'] = "Search Carbon Dioxide data by year."
        menu['3'] = "Search year and see if there is Temperature and Carbon Dioxide data overlap."
        menu['4'] = "The average of the CO2 emissions."
        menu['5'] = "Search a year and see if the CO2 level is above average."
        menu['6'] = "Search a year and see if the CO2 level is below average."
        menu['7'] = "Displays all the Carbon Dioxide data."
        menu['8'] = "Displays all the Temperature data."
        menu['9'] = "Displays both the Carbon Dioxide data and temperature data"
        menu['0'] = "Exit"
        while True:
            options = menu.keys()
            for entry in sorted(options):
                print(entry, menu[entry])
            selection = input("Please Select: ")
            if selection == '1':
                y = []
                val = input("Which year or years do you want to search? Press s to stop\n")
                while True:
                    if val == 's' or val == 'S':
                        break;
                    if (re.search("[12][089][0-9][0-9]{1}$", val) == None) or (
                            re.search("\d{4}", val) == None):  # Using
                        # regular expression to check for valid years
                        print("You entered an invalid year")
                    y.append(val)
                    val = input()
                B.SearchTemperatureByYear(y)
            elif selection == '2':
                y = []
                val = input("Which year or years do you want to search? Press s to stop\n")
                while True:
                    if val == 's' or val == 'S':
                        break;
                    if (re.search("[12][089][0-9][0-9]{1}$", val) == None) or (
                            re.search("\d{4}", val) == None):  # Using regular expression to check for valid years
                        print("You entered an invalid year")
                    y.append(val)
                    val = input()
                B.SearchCarbonDioxideByYear(y)
            elif selection == '3':
                y = []
                val = input("Which year or years do you want to search? Press s to stop\n")
                while True:
                    if val == 's' or val == 'S':
                        break;
                    if (re.search("[12][089][0-9][0-9]{1}$", val) == None) or (
                            re.search("\d{4}", val) == None):  # Using regular expression to check for valid years
                        print("You entered an invalid year")
                        val = input()
                    y.append(val)
                    val = input()
                B.SearchCarbonDioxideAndTemperatureByYear(y)
            elif selection == '4':
                print("The average of the CO2 emission is", B.TheAverageCO2emission())
            elif selection == '5':
                val = input("What year do you want to search?\n")
                while (re.search("[12][09][0-9][0-9]{1}$", val) == None) or (
                        re.search("\d{4}", val) == None):  # Using regular expression to check for valid years
                    print("You entered an invalid year")
                    val = input()
                if B.CheckIfYearIsAboveCO2Average(val) is True:
                    print("{} is above the CO2 average".format(val))
                else:
                    print("{} is not above the CO2 average".format(val))
            elif selection == '6':
                val = input("What year or years do you want to search?\n")
                while (re.search("[12][09][0-9][0-9]{1}$", val) == None) or (
                        re.search("\d{4}", val) == None):  # Using regular expression to check for valid years
                    print("You entered an invalid year")
                    val = input()
                if B.CheckIfYearIsBelowCO2Average(val) is True:
                    print("{} is below the CO2 average".format(val))
                else:
                    print("{} is not below the CO2 average".format(val))
            elif selection == '7':
                self.printoutinfo(**B.CarbonDioxideDatabase)
            elif selection == '8':
                self.printoutinfo(**B.TemperatureDatabase)
            elif selection == '9':
                self.printoutinfo(**B.CO2andTempDatabase)
            elif selection == '0':
                print("Goodbye")
                break
            else:
                print("Unknown Option Selected!\n")