from setlog.domain.entities import Act, Genre, Label, Location


def test_act_entity() -> None:
    genre = Genre(name="Jazz", description="Jazz music")
    label = Label(name="Blue Note", description="Jazz label", location=None)
    loc = Location(continent="North America", country="USA", city="New York")
    act = Act(
        id=1,
        name="Miles Davis",
        description="Legendary jazz musician",
        aliases=["MD", "Miles"],
        genres=[genre],
        labels=[label],
        origin=loc,
    )
    assert act.id == 1
    assert act.name == "Miles Davis"
    assert act.description == "Legendary jazz musician"
    assert "MD" in act.aliases
    assert genre in act.genres
    assert label in act.labels
    assert act.origin == loc
