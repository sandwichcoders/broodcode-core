from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.pickle_storage import store_to_pickle, read_from_pickle, delete_pickles

print(fetch_menu())

store_to_pickle("test", {"test": "123"})
print(read_from_pickle("test"))
delete_pickles(["test"])