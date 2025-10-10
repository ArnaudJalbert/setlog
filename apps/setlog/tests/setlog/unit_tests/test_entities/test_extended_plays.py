from datetime import datetime

from setlog.domain.entities import ExtendedPlay, Label, Track


def test_extended_play_instantiation() -> None:
    track = Track(title="EP Song", duration=120)
    label = Label(name="LabelEP")
    ep = ExtendedPlay(
        title="Test EP",
        tracks=[track],
        release_date=datetime(2021, 5, 5),
        labels={label},
    )
    assert ep.title == "Test EP"
    assert isinstance(ep.tracks[0], Track)
    assert ep.release_date.year == 2021
    assert label in ep.labels
