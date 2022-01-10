from libraries.implementations.factories.pizzahut_veg_pizza_factory import PizzahutVegPizzaFactory 
from libraries.interfaces.pizza import Pizza
from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.client import Client


class PizzahutVegPizzaClient(Client):

	@staticmethod
	def get_pizza() -> Pizza:

		factory: PizzaFactory = PizzahutVegPizzaFactory()
		pizza: Pizza = factory.create_pizza()

		return pizza
