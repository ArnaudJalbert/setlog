from datetime import datetime

from setlog.domain.entities import Album, Label, Track


def test_album_instantiation() -> None:
    track = Track(title="Song 1", duration=180)
    label = Label(name="Label1")
    album = Album(
        title="Test Album",
        tracks=[track],
        release_date=datetime(2020, 1, 1),
        labels={label},
    )
    assert album.title == "Test Album"
    assert isinstance(album.tracks[0], Track)
    assert album.release_date.year == 2020
    assert label in album.labels
