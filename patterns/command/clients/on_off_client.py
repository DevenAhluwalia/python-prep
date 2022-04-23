from clients.client import Client


class OnOrOffClient(Client):

	# def __init__(
	# 	self) -> None:

	# 	super(OnOrOffClient, self).__init__()


	def execute(
		self) -> None:

		for slot_number in [0,1,2]:
			for is_on_command in [True, False]:
				self.remote_control.on_button_pressed(slot_number, is_on_command)
