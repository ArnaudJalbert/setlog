from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from ..value_objects.common_types import ID, Description, Name
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
        id (ID): A unique identifier for the act. This attribute is mandatory.
        name (Name): The name of the act. This attribute is mandatory.
        description (Description): A brief description of the act. This attribute is
            optional and defaults to an empty string.
        origin (Optional[Location | None]): The geographical origin of the act.
            This attribute is optional and can be None if the origin is unknown.
        start_date (Optional[datetime | None]): The date when the act was formed
            or started. This attribute is optional and can be None if the start
            date is unknown.
        end_date (Optional[datetime | None]): The date when the act disbanded or ended.
            This attribute is optional and can be None if the act is still active or
            if the end date is unknown.
        aliases (set[str]): A set of alternative names or aliases for the act.
            This attribute is optional and defaults to an empty set.
        genres (set[Genre]): A set of musical genres associated with the act.
            This attribute is optional and defaults to an empty set.
    """

    id: ID
    name: Name
    description: Optional[Description] = str()
    origin: Optional[Location | None] = None
    start_date: Optional[datetime | None] = None
    end_date: Optional[datetime | None] = None
    aliases: set[str] = field(default_factory=set)
    genres: set[Genre] = field(default_factory=set)

    def __post_init__(self) -> None:
        """Post-initialization processing to validate attributes.

        Raises:
            ValueError: If start_date is after end_date.
        """
        # Validate that start_date is not after end_date
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValueError(
                f"`start_date` ({self.start_date}) cannot be after "
                f"`end_date` ({self.end_date})."
            )
