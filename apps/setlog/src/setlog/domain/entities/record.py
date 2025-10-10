from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .label import Label
from .track import Track


@dataclass(kw_only=True, slots=True)
class Record:
    """A Record represents a music release.

    A release will contain multiple tracks and is associated with one or more labels.

    Attributes:
        title (str): The title of the record.
        tracks (list[Track]): A list of tracks included in the record.
        release_date (datetime): The date when the record was released.
        labels (set[Label]): A set of labels associated with the record.
    """

    title: str
    tracks: list[Track]
    release_date: datetime
    labels: set[Label] = field(default_factory=set)
