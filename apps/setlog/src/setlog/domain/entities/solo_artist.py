from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..value_objects import Name
from .recording_act import RecordingAct


@dataclass(kw_only=True, slots=True)
class SoloArtist(RecordingAct):
    """A solo arist represents a singular musical performer.

    The SoloArtist entity inherits from the RecordingAct class, which encapsulates
    common attributes shared among all recording acts, such as the act's name and
    any associated metadata.

    The recoding artist is characterized by attributes specific to
    individual performers, such as their real name and birthdate.

    Attributes:
        Inherits all attributes from the Act class.
        real_name (Name): The real name of the artist. This attribute is mandatory.
        birthdate (Optional[datetime]): The birthdate of the artist. This attribute
    """

    real_name: Name
    birthdate: datetime | None = None
