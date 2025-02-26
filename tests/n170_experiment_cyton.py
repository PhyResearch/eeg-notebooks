# Imports
from eegnb import generate_save_fn
from eegnb.devices.eeg import EEG
from eegnb.experiments.visual_n170 import n170

# Define some variables
board_name = 'cyton'
experiment = 'visual_n170'
session = 1
subject = 1
record_duration = 120

# Create output filename
save_fn = generate_save_fn(board_name, experiment, subject, session)

# Setup EEG device
eeg_device = EEG(device=board_name)

# Run stimulus presentation
n170.present(duration=record_duration, eeg=eeg_device, save_fn=save_fn)