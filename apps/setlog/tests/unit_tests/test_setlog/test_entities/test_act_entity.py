from datetime import datetime

from setlog.domain.entities import Act
from setlog.domain.entities.genre import Genre
from setlog.domain.entities.location import Location
from setlog.domain.value_objects.common_types import Description, Name


class ConcreteAct(Act):
    """Dummy concrete implementation of the abstract Act class for testing purposes."""

    pass


def test_act_entity_minimal_attributes() -> None:
    act = ConcreteAct(id="act123", name="The Testers")
    assert act.id == "act123"
    assert act.name == "The Testers"
    assert act.description == ""
    assert act.aliases == set()
    assert act.genres == set()
    assert act.origin is None
    assert act.start_date is None
    assert act.end_date is None


def test_act_entity_all_attributes() -> None:
    # Set up genres and location
    genre1 = Genre(name=Name("rock"), description=Description("Rock music"))
    genre2 = Genre(name=Name("pop"), description=Description("Pop music"))
    location1 = Location(continent="Europe", country="France", city="Paris")
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2020, 1, 1)

    # Create the act with all attributes
    act = ConcreteAct(
        id="act123",
        name="The Testers",
        description="A test band",
        start_date=start_date,
        end_date=end_date,
        aliases=["Test Band", "The Testing Group"],
        genres=[genre1, genre2],
        origin=location1,
    )

    # Assertions
    assert act.id == "act123"
    assert act.name == "The Testers"
    assert act.description == "A test band"
    assert act.aliases == ["Test Band", "The Testing Group"]
    assert act.genres == [genre1, genre2]
    assert act.origin == location1
    assert act.start_date == start_date
    assert act.end_date == end_date


def test_start_date_after_end_date() -> None:
    try:
        ConcreteAct(
            id="act123",
            name="The Testers",
            start_date=datetime(2021, 1, 1),
            end_date=datetime(2020, 1, 1),
        )
    except ValueError as e:
        assert (
            str(e) == "`start_date` (2021-01-01 00:00:00) cannot be after "
            "`end_date` (2020-01-01 00:00:00)."
        )
    else:
        assert False, "ValueError was not raised when start_date is after end_date"
