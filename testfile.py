
from collections import defaultdict
from collections import namedtuple
import re


class Database:

    def __init__(self):
        self.Temperature = namedtuple('Temperature',
                                      ['median', 'upper', 'lower'])
        self.TemperatureDatabase = defaultdict(lambda: self.Temperature('0', '0', '0'))

    def ReadTemperature(self):  # Read in the temperature file
        with open('Temperature.csv', 'r') as f:
            Temp = f.readlines()[4:-1]
            for line in Temp:
                fields = re.search(
                    r"(\d{4}).*?([-][0]+[.]\d+|[0]+[.]\d+).*?([-][0]+[.]\d+|[0]+[.]\d+|[0]).*?([-][0]+[.]\d+|[0]+["
                    r".]\d+)",
                    line)
                year = fields.group(1)
                Median = float(fields.group(2))
                Upper = float(fields.group(3))
                Lower = float(fields.group(4))
                T = self.Temperature( Median, Upper, Lower)
                self.TemperatureDatabase[year] = T

    def print(self):
        for i in self.TemperatureDatabase.items():
            print(i)


def main():
    D = Database()
    D.ReadTemperature()
    D.print()


if __name__ == "__main__":
    main()