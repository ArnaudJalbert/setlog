from setlog.domain.entities import Act


class ConcreteAct(Act):
    pass


def test_act_entity() -> None:
    act = ConcreteAct(
        id="act123",
        name="The Testers",
        description="A test band",
        aliases=["Test Band", "The Testing Group"],
        genres=[],
        labels=[],
        origin=None,
    )
    assert act.id == "act123"
    assert act.name == "The Testers"
    assert act.description == "A test band"
    assert act.aliases == ["Test Band", "The Testing Group"]
    assert act.genres == []
    assert act.labels == []
    assert act.origin is None
