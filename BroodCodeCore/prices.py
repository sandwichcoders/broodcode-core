from BroodCodeCore.pickle_storage import store_to_pickle
import json

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

def calculate_price(menu: list, sandwich_props: dict[bread_type_typing], pickle_name: str, fee: int = 0):
    """
    Calculate the price of a sandwich
    Args:
        menu: List of products by category
        sandwich_props: Dictionary of bread types
        pickle_name: The name of the pickle where the calculated data will be stored in
        fee: Optional fee to add to the original price. Default is 0

    Returns:
        Dictionary containing profit, count, product in tuple and the price of the product
    """
    totals = {'profit': 0, 'count': 0}
    updated_menu = {}
    for product in sorted(menu, key=lambda product: product["price"]):
        bread_type_ids = json.loads(product["breadtypes"])
        for bread_type_id in bread_type_ids:
            if bread_type_id not in sandwich_props:
                continue
            org_price = price = round(product["price"] * 100 + sandwich_props[bread_type_id]["surcharge"] * 100)
            while price in codes:
                price += 1
            profit = price - org_price
            totals["profit"] += profit
            totals["count"] += 1

            codes[price] = (product["title"], sandwich_props[bread_type_id]["name"], profit) #TODO: parse breadtypes from JSON to Python
            versions.append(f"{sandwich_props[bread_type_id]['name'].lower()}={price}")

            updated_menu[_format_price(_add_order_fee(price, fee))] = codes[price]

    store_to_pickle(pickle_name, {"products": menu, "codes": updated_menu, "profit": round(totals["profit"] / totals["count"])})
    return updated_menu

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