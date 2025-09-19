from dataclasses import dataclass

from ..value_objects.common_types import Description, Name
from .location import Location


@dataclass
class Label:
    """A Label represents a record label in the music industry.

    Attributes:
        name (str): The name of the label.
        description (str): A brief description of the label.
    """

    name: Name
    description: Description
    location: Location | None
