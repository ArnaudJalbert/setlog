from datetime import datetime

from setlog.domain.entities import SoloArtist
from setlog.domain.value_objects import Name


def test_solo_artist_instantiation() -> None:
    name = Name("Artist Name")
    real_name = Name("Real Name")
    artist = SoloArtist(name=name, real_name=real_name, birthdate=datetime(1990, 1, 1))
    assert artist.real_name == real_name
    assert artist.name == name
    assert artist.birthdate.year == 1990
