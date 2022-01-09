from libraries.interfaces.pizza_factory import pizza_factory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.pizzahut_veg_pizza import VegPizzahutPizza

class pizzahut_veg_pizza_factory(pizza_factory):
	
	@staticmethod
	def create_pizza() -> Pizza:

		result: Pizza = VegPizzahutPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result
	