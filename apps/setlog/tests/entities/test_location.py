from setlog.domain.entities import Location


def test_location_entity() -> None:
    loc = Location(continent="Europe", country="France", city="Paris")
    assert loc.continent == "Europe"
    assert loc.country == "France"
    assert loc.city == "Paris"
