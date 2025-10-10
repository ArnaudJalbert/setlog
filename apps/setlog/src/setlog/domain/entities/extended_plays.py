from __future__ import annotations

from dataclasses import dataclass

from .record import Record


@dataclass(kw_only=True, slots=True)
class ExtendedPlay(Record):
    """An Extended Play (EP) represents a musical recording that contains more
    tracks than a single, but is usually unqualified as an album or LP.

    EPs are typically shorter than full albums.

    Attributes:
        Inherits all attributes from the Record class.
    """
