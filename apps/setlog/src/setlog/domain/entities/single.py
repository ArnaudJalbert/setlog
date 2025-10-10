from __future__ import annotations

from dataclasses import dataclass

from .record import Record


@dataclass(kw_only=True, slots=True)
class Single(Record):
    """A Single represents a type of music release that typically
    features one main track.

    Attributes:
        Inherits all attributes from the Record class.
    """
