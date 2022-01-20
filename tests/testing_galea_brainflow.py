# Imports
import os
from eegnb import generate_save_fn
from eegnb.devices.eeg import EEG
from eegnb.experiments.visual_n170 import n170
from eegnb.analysis.utils import load_data

# Define some variables
#board_name = 'cyton'
board_name = 'galea'
experiment = 'visual_n170'
session = 0o1
subject = 0o1 # a 'very British number'
record_duration=120
dataDir = r'C:\Users\gbern\Documents\GitHub\eeg-notebooks\Data'
# Initiate EEG device
eeg_device = EEG(device=board_name, ip_addr='192.168.5.102')
#eeg_device = EEG(device=board_name, serial_port="COM19")
# Create output filename
save_fn = generate_save_fn(board_name, experiment, subject, session)
eeg_device.start('test01', record_duration)

# Run experiment
# n170.present(duration=record_duration, eeg=eeg_device, save_fn=save_fn)

# start the stream

# Load recorded data
# raw = load_data(subject, session, board_name, experiment)