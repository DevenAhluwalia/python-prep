from libraries.implementations.factories.dominos_veg_pizza_factory import DominosVegPizzaFactory 
from libraries.interfaces.pizza import Pizza
from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.client import Client


class DominosVegPizzaClient(Client):

	@staticmethod
	def get_pizza() -> Pizza:

		factory: PizzaFactory = DominosVegPizzaFactory()
		pizza: Pizza = factory.create_pizza()

		return pizza