from quality_lab.database import Database


def test_database_stores_product():
    db = Database(":memory:")
    try:
        db.add_product("Book", 10)
        assert db.list_products() == [("Book", 10.0)]
    finally:
        db.close()


# TODO: add tests for negative price, empty name, SQL injection text.
