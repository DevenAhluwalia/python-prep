from clients.client import Client


class OnOrOffClient(Client):

	def execute(
		self) -> None:

		for switch in self.switches:

			for is_on_command in [True, False]:

				self.remote_control.on_button_pressed(
					slot_number=switch,
					is_on_command=is_on_command)
