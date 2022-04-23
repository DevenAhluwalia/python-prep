from clients.client import Client


class UndoClient(Client):

	def execute(
		self) -> None:

		self.remote_control.on_button_pressed(
			slot_number=self.light_switch,
			is_on_command=True)

		self.remote_control.on_button_pressed(
			slot_number=self.light_switch,
			is_on_command=False)

		self.remote_control.undo()


		self.remote_control.on_button_pressed(
			slot_number=self.tv_on_off_switch,
			is_on_command=True)

		self.remote_control.undo()


		self.remote_control.undo() # Designed to be idempotent. Multiple undos won't have any effect


		self.remote_control.on_button_pressed(
			slot_number=self.tv_change_channel_number_switch,
			is_on_command=True)

		self.remote_control.on_button_pressed(
			slot_number=self.tv_change_channel_number_switch,
			is_on_command=False)

		self.remote_control.undo()


		self.remote_control.on_button_pressed(
			slot_number=self.fan_on_off_switch,
			is_on_command=True)

		self.remote_control.undo()

		self.remote_control.on_button_pressed(
			slot_number=self.fan_slow_fast_switch,
			is_on_command=False)

		self.remote_control.undo()


