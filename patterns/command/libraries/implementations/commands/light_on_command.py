from libraries.interfaces.command import Command
from libraries.implementations.controls.light_control import LightControl

class LightOnCommand(Command):

	def __init__(
		self,
		control: LightControl) -> None:

		self.control = control


	def execute(
		self) -> None:

		self.control.on()


	def undo(
		self) -> None:

		self.control.off()