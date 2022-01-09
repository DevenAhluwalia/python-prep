from libraries.interfaces.command import Command
from libraries.implementations.controls.tv_control import TvControl

class TvOffCommand(Command):

	def __init__(
		self,
		control: TvControl) -> None:

		self.control = control

		
	def execute(
		self) -> None:

		self.control.off()


	def undo(
		self) -> None:

		self.control.on()