from libraries.interfaces.pizza_factory import pizza_factory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.dominos_veg_pizza import VegDominosPizza

class dominos_veg_pizza_factory(pizza_factory):
	
	@staticmethod
	def create_pizza() -> Pizza:
		
		result: Pizza = VegDominosPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result