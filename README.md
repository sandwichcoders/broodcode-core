# broodcode-core
Core features for the broodcode application in one core package

You can use the broodcode core for yourself to to build your own application around it to place a mass order at your local pizzeria for example.

## Code example
```
from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.pickle_storage import delete_pickles
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

orders = calculate_sandwiches("orders", ["sandwiches"])

print(get_full_info())

print(orders)

delete_pickles(["pickle1", "pickle2"])
```

## Disclaimer!
Some functions used in the core have an underscore prefix like ```_example_function(parameter1)```.
These functions are not meant to be used by the end-developer and may be only used in the core itself. 
I don't forbid you to use these functions, but I am not responsible to any damage to your system as you chose to use these protected functions

## How to use the Broodcode Core
1. Download the release or clone the main branch
2. in the 'broodcode-core-main' folder, copy and paste the 'BroodCodeCore' folder into your project's root folder

### Fetch the menu
Fetch the menu raw from the Broodbode API
```
from BroodCodeCore.fetch import fetch_menu

menu = fetch_menu()
```

### Calculate the prices
Calculate the prices of a category of sandwiches
```
from BroodCodeCore.prices import calculate_price

special = calculate_price(menu["special"], menu["breadtypes"], "special", FEE)
sandwiches = calculate_price(menu["sandwiches"], menu["breadtypes"], "sandwiches", FEE)
paninis = calculate_price(menu["paninis"], menu["breadtypes"], "paninis", FEE)
```

### Calculate the amount of ordered sandwiches
```
from BroodCodeCore.calc_sandwiches import calculate_sandwiches

orders = calculate_sandwiches("orders", ["sandwiches"])
```

### Get information about the Broodcode Core
```
from BroodCodeCore.about import get_full_info

print(get_full_info())
```
