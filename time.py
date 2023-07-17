#!/usr/bin/python3
from datetime import datetime

class Time:
    def __init__(self):
        self.data = datetime.today()

    def New(self):
        return self.__dict__

    def Neme(self):
        return self.__class__.__name__


move = Time()

print(move.New())
print(move.Neme())
