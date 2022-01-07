from libraries.implementations.factories.dominos_nveg_pizza_factory import dominos_nveg_pizza_factory 
from libraries.interfaces.pizza import Pizza

class Client:

	@staticmethod
	def get_pizza() -> Pizza:

		return dominos_nveg_pizza_factory().create_pizza()

