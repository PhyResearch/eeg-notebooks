from eegnb.devices.eeg import EEG

# define the name for the board you are using and call the EEG object
board_name = 'galea'
ip_address = '192.168.5.228'
eeg_device = EEG(device=board_name, ip_addr=ip_address)
duration = 120
session = '0o1'
subject = 0o1 # a 'very British number'
# start the stream
eeg_device.start('Data/test.csv', duration)