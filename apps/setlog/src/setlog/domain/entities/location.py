from dataclasses import dataclass


@dataclass
class Location:
    continent: str
    country: str
    city: str
