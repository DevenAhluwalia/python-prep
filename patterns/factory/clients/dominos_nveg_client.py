from libraries.implementations.factories.dominos_nveg_pizza_factory import DominosNonvegPizzaFactory 
from libraries.interfaces.pizza import Pizza
from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.client import Client


class DominosNonvegPizzaClient(Client):

	@staticmethod
	def get_pizza() -> Pizza:

		factory: PizzaFactory = DominosNonvegPizzaFactory()
		pizza: Pizza = factory.create_pizza()

		return pizza

