from __future__ import annotations

from dataclasses import dataclass

from ..value_objects import Second


@dataclass(kw_only=True, slots=True)
class Track:
    """A Track represents an individual audio recording.

    Attributes:
        title (str): The title of the track.
        duration (Second): The duration of the track in seconds.
    """

    title: str
    duration: Second
