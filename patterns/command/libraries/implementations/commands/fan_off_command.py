from libraries.interfaces.command import Command
from libraries.implementations.controls.fan_control import FanControl

class FanOffCommand(Command):

	def __init__(
		self,
		control: FanControl) -> None:

		self.control = control


	def execute(
		self) -> None:

		self.control.off()


	def undo(
		self) -> None:

		self.control.on()