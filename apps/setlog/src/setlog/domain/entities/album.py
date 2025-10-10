from __future__ import annotations

from dataclasses import dataclass

from .record import Record


@dataclass(kw_only=True, slots=True)
class Album(Record):
    """An Album represents a collection of audio recordings issued as a single item.

    An album typically contains multiple tracks and is longer than a single or
    an extended play (EP).

    It is a type of record that showcases an artist's work over a period of time.

    Attributes:
        Inherits all attributes from the Record class.
    """
