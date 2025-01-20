from collections import defaultdict
from BroodCodeCore.pickle_storage import read_from_pickle

opened_pickles = []

def calculate_sandwiches(orders: str, pickles: list):
    """Calculate the ordered sandwiches

    :param orders: name of the .txt file containing the orders
    :param pickles: list of names of the pickles used to calculate the sandwiches with
    :return:
    """
    try:
        with open(f"{orders}.txt") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(
            "\033[31mCORE ERROR AT 'calc_sandwiches.py' IN 'calculate_sandwiches()':\nCreate a text file with orders with a single order per line, or delete the pickles for a new order round\033[0m"
        )
        return

    for pickle in pickles:
        opened_pickles.append(read_from_pickle(pickle))

    for pickle in opened_pickles:
        _sum_up_sandwiches(lines, pickle)

def _sum_up_sandwiches(lines, data):
    totals = {"profit": 0, "count": 0}
    orders = defaultdict(lambda: defaultdict(int))

    for line in lines:
        if line in data["codes"]:
            title, bread_type, profit = data["codes"][line]
            orders[title][bread_type] += 1
            totals["profit"] += profit
            totals["count"] += 1

    for product in data["products"]:
        o = orders.get(product["title"])
        if o:
            amounts = " ".join(f"{k.lower()}={v}" for k,v in sorted(o.items()))
            print(f"{product['title'].split(':')[0].strip()}: {amounts}")