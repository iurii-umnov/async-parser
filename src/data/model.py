from dataclasses import dataclass

"""
Data model
This class describes data that we parse
All the variables have a str type as we finally write everything in csv
"""


@dataclass
class Car:
    model: str
    year: str
    color: str
    price: str
    mileage: str
    engine: str
    horse_power: str
    transmission: str
