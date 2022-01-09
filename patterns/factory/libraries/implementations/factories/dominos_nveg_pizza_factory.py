from libraries.interfaces.pizza_factory import pizza_factory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.dominos_nonveg_pizza import NonvegDominosPizza

class dominos_nveg_pizza_factory(pizza_factory):
	
	@staticmethod
	def create_pizza() -> Pizza:
		
		result: Pizza = NonvegDominosPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result