from libraries.interfaces.pizza_factory import PizzaFactory
from libraries.interfaces.pizza import Pizza
from libraries.implementations.products.pizzahut_veg_pizza import PizzahutVegPizza

class PizzahutVegPizzaFactory(PizzaFactory):
	
	@staticmethod
	def create_pizza() -> Pizza:

		result: Pizza = PizzahutVegPizza()

		print(f"Kitchen is using ingredients: {','.join(result.ingredients)}")

		return result
	