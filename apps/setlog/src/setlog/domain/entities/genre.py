from dataclasses import dataclass

from ..value_objects.common_types import Description, Name


@dataclass
class Genre:
    """A Genre represents a category of music characterized by a particular style, form,
    or content.

    Attributes:
        name (str): The name of the genre.
        description (str): A brief description of the genre.
    """

    name: Name
    description: Description
