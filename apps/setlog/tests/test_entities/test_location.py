from setlog.domain.entities import Location


def test_location_entity() -> None:
    location = Location(continent="Europe", country="France", city="Paris")
    assert location.continent == "Europe"
    assert location.country == "France"
    assert location.city == "Paris"
