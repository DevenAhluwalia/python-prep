from libraries.implementations.factories.pizzahut_nveg_pizza_factory import PizzahutNonvegPizzaFactory 
from libraries.interfaces.pizza import Pizza
from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.client import Client


class PizzahutNonvegPizzaClient(Client):

	@staticmethod
	def get_pizza() -> Pizza:

		factory: PizzaFactory = PizzahutNonvegPizzaFactory()
		pizza: Pizza = factory.create_pizza()

		return pizza
