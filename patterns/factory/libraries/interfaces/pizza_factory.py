from abc import ABC, abstractmethod
from libraries.interfaces.pizza import Pizza

class PizzaFactory(ABC):
	
	@abstractmethod
	def create_pizza(
		self) -> Pizza:

		pass