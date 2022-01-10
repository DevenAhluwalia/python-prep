from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.dominos_nonveg_pizza import DominosNonvegPizza

class DominosNonvegPizzaFactory(PizzaFactory):
	
	@staticmethod
	def create_pizza() -> Pizza:
		
		result: Pizza = DominosNonvegPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result