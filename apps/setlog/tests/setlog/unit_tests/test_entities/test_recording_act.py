from setlog.domain.entities import Album, ExtendedPlay, RecordingAct, Single


def test_recording_act_collections() -> None:
    album = Album(title="Album", tracks=[], release_date=None, labels=set())
    ep = ExtendedPlay(title="EP", tracks=[], release_date=None, labels=set())
    single = Single(title="Single", tracks=[], release_date=None, labels=set())
    act = RecordingAct(
        name="Test Act",
        albums=[],
        extended_plays=[],
        singles=[],
    )
    act.albums = [album]
    act.extended_plays = [ep]
    act.singles = [single]
    assert isinstance(act.albums[0], Album)
    assert isinstance(act.extended_plays[0], ExtendedPlay)
    assert isinstance(act.singles[0], Single)
