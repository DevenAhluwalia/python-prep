from libraries.interfaces.command import Command

class NoopCommand(Command):

	def execute(
		self) -> None:

		pass


	def undo(
		self) -> None:

		pass