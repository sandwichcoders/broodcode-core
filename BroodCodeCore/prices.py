codes = {}
versions = []

bread_type_typing = {
    'id': int,
    'active': int,
    'autoscore': int,
    'bread_id': int,
    'ranking': int,
    'name': str,
    'surcharge': int,
    'updatedat': str
}

product_typing = {
    'id': int,
    'ranking': int,
    'title': str,
    'subtitle': str,
    'price': int,
    'pricetext': str | None,
    'plasticts_id': int | None,
    'breadtypes': str,
    'gwarn': int,
    'autoscore': int,
    'categorie_id': int,
}

def calculate_price(sandwich_props: dict[bread_type_typing], product: dict[product_typing], fee: int = 0):
    """
    Calculate the price of a sandwich
    Args:
        sandwich_props: The properties of the sandwich
        product: The properties of the product
        fee: Optional fee to add to the original price. Default is 0

    Returns:
        Dictionary containing profit, count, product in tuple and the price of the product
    """
    totals = {'profit': 0, 'count': 0}
    org_price = price = round(product["price"] * 100 + sandwich_props["surcharge"] * 100)
    while price in codes:
        price += 1
    profit = price - org_price
    totals["profit"] += profit
    totals["count"] += 1

    codes[price] = (product["title"], sandwich_props["name"], profit)
    versions.append(f"{sandwich_props['name'].lower()}={price}")

    return {
        "profit": totals["profit"],
        "count": totals["count"],
        "product": codes[price],
        "price": _format_price(_add_order_fee(price, fee)),
    }

def _add_order_fee(price: int, fee: int = 0):
    """
    Add a fee to the original price
    Args:
        price: The original price
        fee: The fee to add to the original price. Default is 0

    Returns:
        The price with fee included
    """
    return price + fee

def _format_price(price: int):
    """
    Converts a price in cents to a formatted string in euros with a comma as the decimal separator.

    Args:
        price (int): The price in cents.

    Returns:
        str: The formatted price in euros, e.g., "6,00" for 600.
    """
    euros = price // 100
    cents = price % 100
    return f"{euros},{cents:02d}"