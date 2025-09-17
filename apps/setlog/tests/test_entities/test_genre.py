from setlog.domain.entities import Genre


def test_genre_entity() -> None:
    genre = Genre(name="Rock", description="A genre of popular music.")
    assert genre.name == "Rock"
    assert genre.description == "A genre of popular music."
