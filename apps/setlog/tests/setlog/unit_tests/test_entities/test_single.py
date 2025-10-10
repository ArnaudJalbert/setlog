from datetime import datetime

from setlog.domain.entities import Label, Single, Track


def test_single_instantiation() -> None:
    track = Track(title="Single Song", duration=150)
    label = Label(name="LabelSingle")
    single = Single(
        title="Test Single",
        tracks=[track],
        release_date=datetime(2022, 2, 2),
        labels={label},
    )
    assert single.title == "Test Single"
    assert isinstance(single.tracks[0], Track)
    assert single.release_date.year == 2022
    assert label in single.labels
