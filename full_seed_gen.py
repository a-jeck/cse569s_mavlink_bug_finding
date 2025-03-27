import os, random, string
from pymavlink import mavutil
from constants import SEED, TYPE_RANGES, MESSAGE_TYPES, MIN, MAX, RAND
from message_encode import create_message
from functions import write_message

output_dir = 'input'
os.makedirs(output_dir, exist_ok=True)

mav = mavutil.mavlink.MAVLink(None)
rng = random.Random(SEED)

# Generate and save messages
for i, msg_type in enumerate(MESSAGE_TYPES):
    msg = create_message(mav, RAND, rng, msg_type)
    if msg:
        write_message(mav, output_dir, i, msg_type, msg)
        