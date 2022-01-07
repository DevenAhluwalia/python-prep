from libraries.interfaces.pizza import Pizza

class VegPizzahutPizza(Pizza):

	@property
	def pizza_name(self):
		return "VegPizzahutPizza"

	@property
	def ingredients(self):
		return ["cheese", "tandoori paneer"]