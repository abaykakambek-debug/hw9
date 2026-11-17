import pytest
from quality_lab.models import Hero, Product


def test_hero_damage_reduces_health():
    hero = Hero("Ada", 100)
    hero.take_damage(20)
    assert hero.health == 80


def test_product_discount():
    product = Product("Book", 100)
    assert product.discounted_price(20) == 80

def test_database_stores_product():
    db = Database(":memory:")
    try:
        db.add_product("Book", 10)
        assert db.list_products() == [("Book", 10.0)]
    finally:
        db.close()

# TODO: add tests for negative initial health, negative price,
# 0/100 percent discount, invalid percent.
