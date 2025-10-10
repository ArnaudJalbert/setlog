from setlog.domain.entities import Track


def test_track_instantiation() -> None:
    track = Track(title="Track Title", duration=123)
    assert track.title == "Track Title"
    assert track.duration == 123
