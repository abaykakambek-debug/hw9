import pytest
from hero import Hero


# 3 граничных теста для Hero
def test_health_not_negative():
    hero = Hero("Ada", health=10)
    hero.hit(15)
    assert hero.health >= 0


def test_hit_zero_damage():
    hero = Hero("Ada", health=10)
    hero.hit(0)
    assert hero.health == 10


def test_hit_negative_damage_raises_error():
    hero = Hero("Ada", health=10)
    with pytest.raises(ValueError):
        hero.hit(-5)


# Тест с monkeypatch и фейковыми данными (для парсера продуктов)
def fake_api_client():
    return {"products": [{"name": "Mock Product", "price": 99}]}


def parse_products(api_client_func):
    data = api_client_func()
    return data.get("products", [])


def test_parse_products_with_monkeypatch(monkeypatch):
    monkeypatch.setattr("__main__.fake_api_client", lambda: {"products": [{"name": "Test Item", "price": 42}]})
    
    products = parse_products(fake_api_client)
    assert len(products) == 1
    assert products[0]["name"] == "Test Item"
    assert products[0]["price"] == 42