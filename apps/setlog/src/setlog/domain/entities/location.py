from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Location:
    """A Location represents a geographical place, typically used to denote the origin
    of a musical act or event. It can also be associated with record labels or
    other entities within the setlog domain.

    We keep the location information simple with just continent, country, and city.

    Attributes:
        continent (str): The continent where the location is situated.
        country (str): The country of the location.
        city (str): The city of the location.
    """

    continent: str
    country: str
    city: str
