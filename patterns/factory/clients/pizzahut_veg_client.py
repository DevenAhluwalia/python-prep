from libraries.implementations.factories.pizzahut_veg_pizza_factory import pizzahut_veg_pizza_factory 
from libraries.interfaces.pizza import Pizza

class Client:

	@staticmethod
	def get_pizza() -> Pizza:

		return pizzahut_veg_pizza_factory().create_pizza()