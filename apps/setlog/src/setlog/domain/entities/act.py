from abc import ABC
from dataclasses import dataclass

from ..value_objects.common_types import ID, Description, Name
from .genre import Genre
from .label import Label
from .location import Location


@dataclass
class Act(ABC):
    """An Act denotes the abstract parent entity of any entity whose role
    is to perform musically.

    It is defined as an abstract class that cannot be instantiated directly
    and must be subclassed by a concrete implementation.

    The Act entity encapsulates the common attributes and behaviors shared by all
    types of musical performers, such as solo artists, bands, orchestras,
    and other musical entities.

    Attributes:
        id (ID): A unique identifier for the act.
        name (Name): The name of the act.
        description (Description): A brief description of the act.
        aliases (set[str]): A set of alternative names or aliases for the act.
        genres (set[str]): A set of musical genres associated with the act.
        labels (set[str]): A set of record labels associated with the act.
        origin (Location | None): The geographical origin of the act,
        it can be None if unknown.
    """

    id: ID
    name: Name
    description: Description
    aliases: list[str]
    genres: list[Genre]
    labels: list[Label]
    origin: Location | None
