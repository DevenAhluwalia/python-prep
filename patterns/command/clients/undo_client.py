from clients.client import Client


class UndoClient(Client):

	def __init__(
		self) -> None:

		super(UndoClient, self).__init__()


	def execute(
		self) -> None:

		
		self.remote_control.on_button_pressed(slot_number=self.light_switch, is_on_command=True)
		self.remote_control.on_button_pressed(slot_number=self.light_switch, is_on_command=False)
		self.remote_control.undo()

		self.remote_control.on_button_pressed(slot_number=self.tv_switch, is_on_command=True)
		self.remote_control.undo()

		self.remote_control.undo()

