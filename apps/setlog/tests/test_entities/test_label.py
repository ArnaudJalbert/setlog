from setlog.domain.entities import Label, Location


def test_label_entity() -> None:
    location = Location(continent="Europe", country="UK", city="London")
    label = Label(name="EMI", description="Major record label", location=location)
    assert label.name == "EMI"
    assert label.description == "Major record label"
    assert label.location == location
