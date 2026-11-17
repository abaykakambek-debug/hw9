import logging
from .exceptions import BotDataError

logger = logging.getLogger(__name__)


def parse_products(fetch_json):
    """fetch_json is a callable returning a Python dict; no network required."""
    try:
        payload = fetch_json()
    except Exception as exc:
        logger.error("Product source failed: %s", type(exc).__name__)
        raise BotDataError("Could not load product data") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("products"), list):
        raise BotDataError("Expected object with a products list")
    result = []
    for item in payload["products"]:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            raise BotDataError("Product must have a string name")
        price = item.get("price")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise BotDataError("Product price must be nonnegative number")
        result.append({"name": item["name"], "price": price})
    logger.info("Parsed %d products", len(result))
    return result
