import requests
import json
from datetime import date
from BroodCodeCore.clippy import Clippy
clippy = Clippy()

def fetch_menu():
    try:
        response = requests.get(
            f"https://bestellen.broodbode.nl/v2-2/pccheck/null/{date.today()}/afhalen/8?cb=1695969466297",
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
            },
            timeout=10,  # Timeout after 10 seconds
        )
    except requests.exceptions.Timeout:
        clippy.c_print("CORE ERROR: The request timed out. Please try again later.")
        return {"products": [], "breadtypes": {}}
    except requests.exceptions.RequestException as e:
        clippy.c_print(f"CORE ERROR: An error occurred: {e}")
        return {"products": [], "breadtypes": {}}

    data = response.json()
    products = data["products"]
    bread_types_by_id = {b["id"]: b for b in data["breadtypes"]}

    full_menu = {"products": products, "breadtypes": bread_types_by_id}

    _strip_menu(full_menu)

    return {"products": products, "breadtypes": bread_types_by_id}

def _strip_menu(full_menu):
    stripped_menu = []
    for product in sorted(full_menu["products"], key=lambda product: product["price"]):
        if not product["breadtypes"]:
            continue
        if "special van de week" in product["title"].lower():
            continue  # Skip 'Special van de week'
        compatible_bread_type_ids = json.loads(product["breadtypes"])
        if 41 not in compatible_bread_type_ids:
            continue
        stripped_menu.append(product)
    return stripped_menu