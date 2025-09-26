from dataclasses import dataclass

from ..value_objects.common_types import Description, Name


@dataclass
class Genre:
    """A Genre represents a category of music characterized by a particular style, form,
    or content.

    Attributes:
        name (Name): The name of the genre.
        description (Description): A brief description of the genre.
    """

    name: Name
    description: Description

    def __hash__(self) -> int:
        """Generates a hash value for the Genre instance based on its attributes.

        The hash is computed using a tuple of the name and description attributes.

        Returns:
            The hash value of the Genre instance.
        """
        return hash((self.name, self.description))
