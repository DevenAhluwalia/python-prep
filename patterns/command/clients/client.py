from libraries.remote_control import RemoteControl

from libraries.implementations.controls.fan_control import FanControl
from libraries.implementations.controls.tv_control import TvControl
from libraries.implementations.controls.light_control import LightControl

from libraries.implementations.commands.fan_on_command import FanOnCommand
from libraries.implementations.commands.fan_off_command import FanOffCommand
from libraries.implementations.commands.fan_slow_command import FanSlowCommand
from libraries.implementations.commands.fan_fast_command import FanFastCommand

from libraries.implementations.commands.tv_on_command import TvOnCommand
from libraries.implementations.commands.tv_off_command import TvOffCommand
from libraries.implementations.commands.tv_increase_channel_number_command import TvIncreaseChannelNumberCommand
from libraries.implementations.commands.tv_decrease_channel_number_command import TvDecreaseChannelNumberCommand

from libraries.implementations.commands.light_on_command import LightOnCommand
from libraries.implementations.commands.light_off_command import LightOffCommand


class Client:

	def __init__(
		self):

		self.fan_on_off_switch   			 = 0
		self.fan_slow_fast_switch   		 = 1

		self.tv_on_off_switch    			 = 2
		self.tv_change_channel_number_switch = 3

		self.light_switch 					 = 4

		self.switches = [
			self.fan_on_off_switch, 
			self.fan_slow_fast_switch,
			self.tv_on_off_switch, 
			self.tv_change_channel_number_switch, 
			self.light_switch
		]

		fan_control   = FanControl()
		tv_control 	  = TvControl()
		light_control = LightControl()

		fan_on_command 	 = FanOnCommand(control=fan_control)
		fan_off_command  = FanOffCommand(control=fan_control)
		fan_slow_command = FanSlowCommand(control=fan_control)
		fan_fast_command = FanFastCommand(control=fan_control)

		tv_on_command 							= TvOnCommand(control=tv_control)
		tv_off_command 							= TvOffCommand(control=tv_control)
		tv_increase_channel_number_command 		= TvIncreaseChannelNumberCommand(control=tv_control)
		tv_decrease_channel_number_command		= TvDecreaseChannelNumberCommand(control=tv_control)

		light_on_command  = LightOnCommand(control=light_control)
		light_off_command = LightOffCommand(control=light_control)

		remote_control = RemoteControl(
			num_of_slotes=len(self.switches))

		remote_control.set_command(
			slot_number=self.fan_on_off_switch,
			on_command=fan_on_command,
			off_command=fan_off_command)

		remote_control.set_command(
			slot_number=self.fan_slow_fast_switch,
			on_command=fan_fast_command,
			off_command=fan_slow_command)

		remote_control.set_command(
			slot_number=self.tv_on_off_switch,
			on_command=tv_on_command,
			off_command=tv_off_command)

		remote_control.set_command(
			slot_number=self.tv_change_channel_number_switch,
			on_command=tv_increase_channel_number_command,
			off_command=tv_decrease_channel_number_command)

		remote_control.set_command(
			slot_number=self.light_switch,
			on_command=light_on_command,
			off_command=light_off_command)

		self.remote_control: RemoteControl = remote_control