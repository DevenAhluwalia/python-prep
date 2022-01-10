from libraries.interfaces.pizza import Pizza

class PizzahutNonvegPizza(Pizza):

	@property
	def pizza_name(self):
		return "NonvegPizzahutPizza"

	@property
	def ingredients(self):
		return ["fish", "eggos"]