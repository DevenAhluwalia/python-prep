from libraries.interfaces.pizza import Pizza

class DominosVegPizza(Pizza):

	@property
	def pizza_name(self):
		return "VegDominosPizza"

	@property
	def ingredients(self):
		return ["pineapple", "guacamole", "paneer"]