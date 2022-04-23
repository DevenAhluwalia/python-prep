from libraries.interfaces.command import Command
from libraries.implementations.commands.noop_command import NoopCommand

class RemoteControl:

		def __init__(
			self,
			num_of_slotes: int=4) -> None:

			self.on_controls = [NoopCommand] * num_of_slotes
			self.off_controls = [NoopCommand] * num_of_slotes
			self.undo_command = NoopCommand


		def set_command(
			self,
			slot_number,
			on_command: Command,
			off_command: Command) -> None:

			self.on_controls[slot_number] = on_command
			self.off_controls[slot_number] = off_command


		def on_button_pressed(
			self,
			slot_number: int,
			is_on_command: bool):

			_command = self.on_controls[slot_number] if is_on_command else self.off_controls[slot_number]

			self.undo_command = _command

			_command.execute()


		def undo(
			self):

			print()
			print(f"Undoing last run command: {type(self.undo_command).__name__}")

			self.undo_command.undo()
			print()