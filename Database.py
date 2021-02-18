from CarbonDioxide import CarbonDioxide
from Temperature import Temperature
from collections import defaultdict
from collections import namedtuple
import re


class Database:

    def __init__(self):
        self.CarbonDioxideDatabase = defaultdict(lambda: CarbonDioxide('0', '0', '0', '0', '0', '0'))
        self.TemperatureDatabase = defaultdict(lambda: Temperature('0', '0', '0', '0'))
        self.CarbonDioxideAndTemperature = namedtuple('Carbon_Dioxide_and_Temperature',
                                        ['decimal', 'average', 'interpolated',
                                         'trend', 'days','median','upper','lower'])
        self.CO2andTempDatabase = defaultdict(
            lambda: self.CarbonDioxideAndTemperature('0','0','0','0','0','0','0','0'))

    def ReadTemperature(self):  # Read in the temperature file
        with open('Temperature.html', 'r') as f:
            Temp = f.readlines()[5:-1]
            for line in Temp:
                fields = re.search(
                    r"(\d{4}).*?([-][0]+[.]\d+|[0]+[.]\d+).*?([-][0]+[.]\d+|[0]+[.]\d+|[0]).*?([-][0]+[.]\d+|[0]+["
                    r".]\d+)",
                    line)
                year = fields.group(1)
                Median = float(fields.group(2))
                Upper = float(fields.group(3))
                Lower = float(fields.group(4))
                T = Temperature( Median, Upper, Lower)
                self.TemperatureDatabase[year] = T

    def ReadCarbonEmission(self):
        with open('CO2.html', 'r') as f:
            month = 0  # counter variable to keep track of the month
            average_decimal = 0  # sum to sum up the decimal column
            average_average = 0  # sum to sum up the average column
            average_interpolated = 0  # sum to sum up the interpolated column
            average_trend = 0  # sum to sum up the trend column
            for line in f.readlines()[4:-1]:
                fields = re.search(
                    r"([34]{1}\d{2}[.]\d{2}|[-]99[.]99).*?([34]{1}\d{2}[.]\d{2}).*?([34]{1}\d{2}[.]\d{2})",
                    line)  # Used Regex to parse the html file
                year = re.search(r"\d{4}", line)
                decimal = re.search(r"\d{4}[.]\d{3}", line)
                average_decimal += float(decimal.group())
                average_average += float(fields.group(1))
                average_interpolated += float(fields.group(2))
                average_trend += float(fields.group(3))
                month += 1
                if month == 12 or (year.group() == '2019' and month == 11): #2019 only has 11 months
                    S = CarbonDioxide( round(average_decimal / month, 3),
                                      round(average_average / month, 2), round(average_interpolated / month, 2),
                                      round(average_trend / month, 2),
                                      -1)
                    self.CarbonDioxideDatabase[year.group()] = S
                    average_decimal = 0  # reset all counter variables
                    average_average = 0
                    average_interpolated = 0
                    average_trend = 0
                    month = 0


    def ReadTemperature(self):  # Read in the temperature file
        with open('Temperature.html', 'r') as f:
            Temp = f.readlines()[5:-1]
            for line in Temp:
                fields = re.search(
                    r"(\d{4}).*?([-][0]+[.]\d+|[0]+[.]\d+).*?([-][0]+[.]\d+|[0]+[.]\d+|[0]).*?([-][0]+[.]\d+|[0]+["
                    r".]\d+)",
                    line)
                year = fields.group(1)
                Median = float(fields.group(2))
                Upper = float(fields.group(3))
                Lower = float(fields.group(4))
                T = Temperature( Median, Upper, Lower)
                self.TemperatureDatabase[year] = T

    def FillinCO2andTempdata(self):
        for i in self.TemperatureDatabase.keys():
            if i in self.TemperatureDatabase.keys() and i in self.CarbonDioxideDatabase.keys():
                s = self.CarbonDioxideAndTemperature(self.CarbonDioxideDatabase[i].C.decimal,
                                                     self.CarbonDioxideDatabase[i].C.average,
                                                     self.CarbonDioxideDatabase[i].C.interpolated,
                                                     self.CarbonDioxideDatabase[i].C.trend,
                                                     self.CarbonDioxideDatabase[i].C.days,
                                                     self.TemperatureDatabase[i].T.median,
                                                     self.TemperatureDatabase[i].T.upper,
                                                     self.TemperatureDatabase[i].T.lower)
                self.CO2andTempDatabase[i] = s


    def SearchTemperatureByYear(self,
                                *args):  # Shows The average emission level and temperature difference of that year
        for x in args[0]:
            if x in self.TemperatureDatabase.keys():
                print("Temperature data of the year {} is {}".format(x,self.TemperatureDatabase[x]))


    def SearchCarbonDioxideByYear(self,
                                  *args):  # Shows The average emission level and temperature difference of that year
        for x in args[0]:
            if x in self.CarbonDioxideDatabase.keys():
                print("Carbon Dioxide data of the year {} is {}".format(x,self.CarbonDioxideDatabase[x]))

    def SearchCarbonDioxideAndTemperatureByYear(self, *args):
        for x in args[0]:
            if x in self.CarbonDioxideDatabase.keys() and x in self.TemperatureDatabase.keys():
                print("Carbon Dioxide and temperature data of the year {} is {}".format(x,self.CO2andTempDatabase[x]))

    def CheckIfYearIsAboveCO2Average(self, year):
        if self.CO2andTempDatabase[year].average > self.TheAverageCO2emission():
            return True
        return False

    def CheckIfYearIsBelowCO2Average(self, year):
        if self.CO2andTempDatabase[year].average < self.TheAverageCO2emission():
            return True
        return False

    def TheAverageCO2emission(self):
        count = 0
        sum = 0
        for i in self.CarbonDioxideDatabase:
            sum += self.CarbonDioxideDatabase[i].C.average
            count +=1
        return round(sum / count, 2)