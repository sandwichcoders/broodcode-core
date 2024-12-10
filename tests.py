from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.pickle_storage import store_to_pickle, read_from_pickle, delete_pickles
from BroodCodeCore.calc_sandwiches import calculate_sandwiches

menu = fetch_menu()
print(menu)

store_to_pickle("test", menu)
print(read_from_pickle("test"))

calculate_sandwiches("orders", ["test"])