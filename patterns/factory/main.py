from libraries.interfaces.pizza import Pizza

from clients.dominos_veg_client import Client as DominosVegPizzaClient
from clients.dominos_nveg_client import Client as DominosNonvegPizzaClient
from clients.pizzahut_veg_client import Client as PizzahutVegPizzaClient
from clients.pizzahut_nveg_client import Client as PizzahutNonvegPizzaClient


dominos_veg_pizza: Pizza = DominosVegPizzaClient().get_pizza()
dominos_veg_pizza.describe()
print()

dominos_nveg_pizza: Pizza = DominosNonvegPizzaClient().get_pizza()
dominos_nveg_pizza.describe()
print()

pizzahut_veg_pizza: Pizza = PizzahutVegPizzaClient().get_pizza()
pizzahut_veg_pizza.describe()
print()

pizzahut_nveg_pizza: Pizza = PizzahutNonvegPizzaClient().get_pizza()
pizzahut_nveg_pizza.describe()
print()