from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.pickle_storage import store_to_pickle, read_from_pickle, delete_all_pickles
from BroodCodeCore.calc_sandwiches import calculate_sandwiches
from BroodCodeCore.prices import calculate_price
from BroodCodeCore.about import get_full_info

FEE: int = 50

menu = fetch_menu()
print(menu)

store_to_pickle("menu_raw", menu)
print(read_from_pickle("menu_raw"))

special = calculate_price(menu["special"], menu["breadtypes"], "special", FEE)
sandwiches = calculate_price(menu["sandwiches"], menu["breadtypes"], "sandwiches", FEE)
paninis = calculate_price(menu["paninis"], menu["breadtypes"], "paninis", FEE)

store_to_pickle("forgotten", {'sandwich_name': "Chengdu Chicken", 'ordered_by': "Hans Landa"}, False)
store_to_pickle("forgotten", {'sandwich_name': "Carpaccio Truffel", 'ordered_by': "Tyler Durden"}, False)

orders = calculate_sandwiches("orders", ["sandwiches"])

print(get_full_info())

print(orders)

delete_all_pickles()

print("Done :D")
