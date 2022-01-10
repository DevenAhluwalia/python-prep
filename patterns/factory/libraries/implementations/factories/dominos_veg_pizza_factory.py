from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.dominos_veg_pizza import DominosVegPizza

class DominosVegPizzaFactory(PizzaFactory):
	
	@staticmethod
	def create_pizza() -> Pizza:
		
		result: Pizza = DominosVegPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result