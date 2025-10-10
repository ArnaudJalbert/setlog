from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime

from ..value_objects.act_types import Description, Name
from .genre import Genre
from .location import Location


@dataclass(kw_only=True, slots=True)
class Act(ABC):
    """An Act denotes the abstract parent entity of any entity whose role
    is to perform musically.

    It is defined as an abstract class that cannot be instantiated directly
    and must be subclassed by a concrete implementation.

    The Act entity encapsulates the common attributes and behaviors shared by all
    types of musical performers, such as solo artists, bands, orchestras,
    and other musical entities.

    Attributes:
        name (Name): The name of the act. This attribute is mandatory.
        description (Description | None): A brief description of the act.
        origin (Location | None): The geographical origin of the act.
        start_date (datetime | None): The date when the act was formed or started.
        end_date (datetime | None): The date when the act disbanded or ended,
            if applicable.
        aliases (set[str]): A set of alternative names or aliases for the act.
        genres (set[Genre]): A set of musical genres associated with the act.
    """

    name: Name
    description: Description | None = None
    origin: Location | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    aliases: set[str] = field(default_factory=set)
    genres: set[Genre] = field(default_factory=set)

    def __post_init__(self) -> None:
        """Post-initialization processing to validate attributes.

        The following validations are performed:
            - Ensures that `start_date` is not after `end_date` if both are provided.

        Raises:
            ValueError: If start_date is after end_date.
        """
        # Validate that start_date is not after end_date
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValueError(
                f"`start_date` ({self.start_date}) cannot be after "
                f"`end_date` ({self.end_date})."
            )
