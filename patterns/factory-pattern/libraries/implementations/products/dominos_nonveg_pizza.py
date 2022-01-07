from libraries.interfaces.pizza import Pizza

class NonvegDominosPizza(Pizza):

	@property
	def pizza_name(self):
		return "NonvegDominosPizza"

	@property
	def ingredients(self):
		return ["bacon", "chicken", "pork"]