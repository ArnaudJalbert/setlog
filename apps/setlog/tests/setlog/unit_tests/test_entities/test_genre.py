from setlog.domain.entities import Genre


def test_genre_entity() -> None:
    genre = Genre(name="Rock", description="A genre of popular music.")
    assert genre.name == "Rock"
    assert genre.description == "A genre of popular music."


def test_genre_entity_hash() -> None:
    genre1 = Genre(name="Rock", description="A genre of popular music.")
    genre2 = Genre(name="Rock", description="Another description.")
    genre3 = Genre(name="Jazz", description="A different genre.")
    genre4 = Genre(name="Rock", description="A genre of popular music.")

    assert hash(genre1) != hash(
        genre2
    )  # Same name but different descriptions, should have different hashes
    assert hash(genre1) != hash(genre3)  # Different names, should have different hashes
    assert hash(genre1) == hash(
        genre4
    )  # Same name and description, should have same hashes
