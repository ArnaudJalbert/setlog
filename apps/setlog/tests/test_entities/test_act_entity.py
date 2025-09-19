from setlog.domain.entities import Act
from setlog.domain.entities.genre import Genre
from setlog.domain.entities.label import Label
from setlog.domain.entities.location import Location
from setlog.domain.value_objects.common_types import Name, Description


class ConcreteAct(Act):
    pass


def test_act_entity() -> None:
    genre1 = Genre(name=Name("rock"), description=Description("Rock music"))
    genre2 = Genre(name=Name("pop"), description=Description("Pop music"))
    location1 = Location(continent="Europe", country="France", city="Paris")
    location2 = Location(continent="North America", country="USA", city="New York")
    label1 = Label(
        name=Name("Test Records"),
        description=Description("A test label"),
        location=location1,
    )
    label2 = Label(
        name=Name("Sample Label"),
        description=Description("Another label"),
        location=location2,
    )

    act = ConcreteAct(
        id="act123",
        name="The Testers",
        description="A test band",
        aliases=["Test Band", "The Testing Group"],
        genres=[genre1, genre2],
        labels=[label1, label2],
        origin=None,
    )
    assert act.id == "act123"
    assert act.name == "The Testers"
    assert act.description == "A test band"
    assert act.aliases == ["Test Band", "The Testing Group"]
    assert act.genres == [genre1, genre2]
    assert act.labels == [label1, label2]
    assert act.labels[0].location == location1
    assert act.labels[1].location == location2
    assert act.origin is None
