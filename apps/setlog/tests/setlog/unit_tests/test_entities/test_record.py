from datetime import datetime

from setlog.domain.entities import Label, Record, Track


def test_record_instantiation() -> None:
    track = Track(title="Record Song", duration=200)
    label = Label(name="LabelRecord")
    record = Record(
        title="Test Record",
        tracks=[track],
        release_date=datetime(2019, 7, 7),
        labels={label},
    )
    assert record.title == "Test Record"
    assert isinstance(record.tracks[0], Track)
    assert record.release_date.year == 2019
    assert label in record.labels
