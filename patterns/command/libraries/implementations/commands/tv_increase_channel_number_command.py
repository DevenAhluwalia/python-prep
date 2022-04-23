from libraries.interfaces.command import Command
from libraries.implementations.controls.tv_control import TvControl

class TvIncreaseChannelNumberCommand(Command):

	def __init__(
		self,
		control: TvControl) -> None:

		self.control = control

		
	def execute(
		self) -> None:

		self.control.increase_channel_number()


	def undo(
		self) -> None:

		self.control.decrease_channel_number()