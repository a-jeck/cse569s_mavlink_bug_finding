import os, random, string
from pymavlink import mavutil
from constants import SEED, TYPE_RANGES, MESSAGE_TYPES, MIN, MAX, RAND
from message_encode import create_message
from functions import write_message
from pymavlink.dialects.v20 import common as mavlink2

output_dir = 'input'
os.makedirs(output_dir, exist_ok=True)

# mav = mavutil.mavlink.MAVLink(None)
mav = mavlink2.MAVLink(None)
rng = random.Random(SEED)

print(create_message(mav, MAX, rng, 'COLLISION'))


# Generate and save messages
# for i, msg_type in enumerate(MESSAGE_TYPES):
#     # rand_msg = create_message(mav, RAND, rng, msg_type)
#     # if rand_msg:
#     #     write_message(mav, output_dir, i, msg_type, RAND, rand_msg)
    
#     max_msg = create_message(mav, MAX, rng, msg_type)
#     if max_msg:
#         write_message(mav, output_dir, i, msg_type, MAX, max_msg)

#     min_msg = create_message(mav, MIN, rng, msg_type)
#     if min_msg:
#         write_message(mav, output_dir, i, msg_type, MIN, min_msg)
    
