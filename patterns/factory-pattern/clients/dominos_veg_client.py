from libraries.implementations.factories.dominos_veg_pizza_factory import dominos_veg_pizza_factory 
from libraries.interfaces.pizza import Pizza

class Client:

	@staticmethod
	def get_pizza() -> Pizza:

		return dominos_veg_pizza_factory().create_pizza()