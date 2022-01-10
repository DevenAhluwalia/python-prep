from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.pizzahut_nonveg_pizza import PizzahutNonvegPizza

class PizzahutNonvegPizzaFactory(PizzaFactory):
	
	@staticmethod
	def create_pizza() -> Pizza:

		result: Pizza = PizzahutNonvegPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result
	