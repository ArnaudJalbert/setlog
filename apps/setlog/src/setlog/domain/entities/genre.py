from __future__ import annotations

from dataclasses import dataclass

from ..value_objects.act_types import Description, Name


@dataclass(kw_only=True, slots=True)
class Genre:
    """A Genre represents a category of music characterized by a particular style, form,
    or content.

    Attributes:
        name (Name): The name of the genre.
        description (Description | None): A brief description of the genre, optional.
    """

    name: Name
    description: Description | None = None

    def __hash__(self) -> int:
        """Generates a hash value for the Genre instance based on its attributes.

        The hash is computed using a tuple of the name and description attributes.

        Returns:
            The hash value of the Genre instance.
        """
        return hash((self.name, self.description))
