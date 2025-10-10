from __future__ import annotations

from dataclasses import dataclass, field

from .act import Act
from .album import Album
from .extended_plays import ExtendedPlay
from .single import Single


@dataclass(kw_only=True, slots=True)
class RecordingAct(Act):
    """A class representing an act that records music.

    This class inherits from the Act class, thereby acquiring all attributes
    and behaviors defined in the Act class. This includes properties such as name,
    description, origin, start and end dates, aliases, and genres.

    Attributes:
        Inherits all attributes from the Act class.

    """

    albums: list[Album] = field(default_factory=list)
    extended_plays: list[ExtendedPlay] = field(default_factory=list)
    singles: list[Single] = field(default_factory=list)
