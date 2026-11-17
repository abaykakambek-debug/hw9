import pytest
from quality_lab.parser import parse_products
from quality_lab.exceptions import BotDataError


def test_parser_fake_response_without_internet():
    fake_fetch = lambda: {"products": [{"name": "Book", "price": 10}]}
    assert parse_products(fake_fetch) == [{"name": "Book", "price": 10}]


def test_parser_rejects_missing_key():
    with pytest.raises(BotDataError):
        parse_products(lambda: {})


# TODO: add empty list, malformed values, and source exception tests.
