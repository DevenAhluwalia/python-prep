from abc import ABC, abstractmethod

class pizza_factory(ABC):
	
	@abstractmethod
	def create_pizza(self, pizza_type):
		pass
	
class pizza_house:
	
	@staticmethod
	def get_pizza(_pizza_house, _pizza_type):
		
		pizza = None
		if _pizza_house == "dominos":
			pizza = dominos_pizza_factory.get_pizza(_pizza_type)
		elif _pizza_house == "pizzahut":
			pizza = pizzahut_pizza_factory.get_pizza(_pizza_type)
		else: raise()
		
		return pizza
		
class dominos_pizza_factory(pizza_factory):
	
	@staticmethod
	def get_pizza(pizza_type):
		
		result = None
		if pizza_type == "veg":
			result = VegDominosPizza()
		elif pizza_type == "nonveg":
			result = NonvegDominosPizza()
		else: raise()
		
		return result
			
class pizzahut_pizza_factory(pizza_factory):
	
	@staticmethod
	def get_pizza(pizza_type):
		
		result = None
		if pizza_type == "veg":
			result = VegPizzahutPizza()
		elif pizza_type == "nonveg":
			result = NonvegPizzahutPizza()
		else: raise()
		
		return result
		
class Pizza:
	
	def describe(self) -> None:
		print(self.pizza_name or "None")
	
class VegDominosPizza(Pizza):

	def __init__(self):
		self.pizza_name = "VegDominosPizza"
		
class NonvegDominosPizza(Pizza):

	def __init__(self):
		self.pizza_name = "NonvegDominosPizza"
	
class VegPizzahutPizza(Pizza):

	def __init__(self):
		self.pizza_name = "VegPizzahutPizza"
	
class NonvegPizzahutPizza(Pizza):

	def __init__(self):
		self.pizza_name = "NonvegPizzahutPizza"
	

pizza = pizza_house.get_pizza(_pizza_house="dominos", _pizza_type="veg")
pizza.describe()

pizza = pizza_house.get_pizza(_pizza_house="dominos", _pizza_type="nonveg")
pizza.describe()

pizza = pizza_house.get_pizza(_pizza_house="pizzahut", _pizza_type="veg")
pizza.describe()

pizza = pizza_house.get_pizza(_pizza_house="pizzahut", _pizza_type="veg")
pizza.describe()