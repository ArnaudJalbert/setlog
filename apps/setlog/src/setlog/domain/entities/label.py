from __future__ import annotations

from dataclasses import dataclass

from ..value_objects.act_types import Description, Name
from .location import Location


@dataclass(kw_only=True, slots=True)
class Label:
    """A Label represents a record label in the music industry.

    Attributes:
        name (str): The name of the label.
        description (str): A brief description of the label.
        location (Location | None): The location of the label, optional.
    """

    name: Name
    description: Description | None = None
    location: Location | None = None

    def __hash__(self) -> int:
        """Generates a hash value for the Label instance based on its attributes.

        The hash is computed using a tuple of the name and description attributes.

        Returns:
            The hash value of the Label instance.
        """
        return hash(self.name)
