from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.pickle_storage import store_to_pickle, read_from_pickle, delete_pickles
from BroodCodeCore.calc_sandwiches import calculate_sandwiches
from BroodCodeCore.prices import calculate_price

menu = fetch_menu()
print(menu)

store_to_pickle("menu_raw", menu)
print(read_from_pickle("menu_raw"))

menu = calculate_price(menu["sandwiches"], menu["breadtypes"], 50)

calculate_sandwiches("orders", ["menu_raw"])