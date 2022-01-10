from libraries.interfaces.pizza import Pizza
from libraries.interfaces.client import Client

from clients.dominos_veg_client import DominosVegPizzaClient
from clients.dominos_nveg_client import DominosNonvegPizzaClient
from clients.pizzahut_veg_client import PizzahutVegPizzaClient
from clients.pizzahut_nveg_client import PizzahutNonvegPizzaClient


class Main:

	@staticmethod
	def runner() -> None:

		dominos_veg_pizza_client: Client = DominosVegPizzaClient()
		dominos_veg_pizza: Pizza = dominos_veg_pizza_client.get_pizza()
		dominos_veg_pizza.describe()
		print()

		dominos_nveg_pizza_client: Client = DominosNonvegPizzaClient()
		dominos_nveg_pizza: Pizza = dominos_nveg_pizza_client.get_pizza()
		dominos_nveg_pizza.describe()
		print()

		pizzahut_veg_pizza_client: Client = PizzahutVegPizzaClient()
		pizzahut_veg_pizza: Pizza = pizzahut_veg_pizza_client.get_pizza()
		pizzahut_veg_pizza.describe()
		print()

		pizzahut_nveg_pizza_client: Client = PizzahutNonvegPizzaClient()
		pizzahut_nveg_pizza: Pizza = pizzahut_nveg_pizza_client.get_pizza()
		pizzahut_nveg_pizza.describe()
		print()

Main.runner()