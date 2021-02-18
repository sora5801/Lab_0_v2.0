from collections import namedtuple
import re


class CarbonDioxide:

    def __init__(self, decimal=0, average=0, interpolated=0, trend=0, days=0, **kwargs):
        self.CarbonDioxide = namedtuple('Carbon_Dioxide',
                                        [ 'decimal', 'average', 'interpolated', 'trend', 'days'])
        self.C = self.CarbonDioxide(decimal, average, interpolated, trend, days)

    def __str__(self):
        return "CarbonDioxide(decimal='{}', average='{}', interpolated='{}', trend='{}', #days='{})".format(self.C.decimal,
                                                                         self.C.average, self.C.interpolated, self.C.trend, self.C.days)

    def __repr__(self):
        return "CarbonDioxide(decimal='{}', average='{}', interpolated='{}', trend='{}', #days='{})".format(
             self.C.decimal,
            self.C.average, self.C.interpolated, self.C.trend, self.C.days)

    def __eq__(self,other):
        self.C = other

    def __iter__(self):
        return self

