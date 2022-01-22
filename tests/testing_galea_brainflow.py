from eegnb.devices.eeg import EEG
from eegnb import generate_save_fn
from eegnb.devices.eeg import EEG
from eegnb.experiments.visual_n170 import n170
# define the name for the board you are using and call the EEG object
# board_name = 'galea'
board_name = 'cyton'
# ip_address = '192.168.5.228'
experiment = 'visual_n170'
#eeg_device = EEG(device=board_name, ip_addr=ip_address)
eeg_device = EEG(device=board_name)
record_duration = 120
session = '0o1'
subject = 0o1 # a 'very British number'

save_fn = generate_save_fn(board_name, experiment, subject, 1)

# start the stream
# eeg_device.start(save_fn, duration)
n170.present(duration=record_duration, eeg=eeg_device, save_fn=save_fn)
