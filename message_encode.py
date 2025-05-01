import ctypes
from pymavlink import mavutil
from functions import value_of_type, random_string
from constants import MIN, MAX, RAND


# Function to create a MAVLink message
def create_message(mav, val_type, rng, msg_type):
    if msg_type == 'SYS_STATUS':
        return mav.sys_status_encode(
            value_of_type('uint32_t', val_type, rng),  
            value_of_type('uint32_t', val_type, rng),
            value_of_type('uint32_t', val_type, rng),  
            value_of_type('int', val_type, rng, 0, 1000), 
            value_of_type('uint16_t', val_type, rng),  
            value_of_type('int16_t', val_type, rng),  
            value_of_type('int8_t', val_type, rng),  
            value_of_type('uint16_t', val_type, rng),  
            value_of_type('uint16_t', val_type, rng),  
            value_of_type('uint16_t', val_type, rng),  
            value_of_type('uint16_t', val_type, rng),  
            value_of_type('uint16_t', val_type, rng),  
            value_of_type('uint16_t', val_type, rng), 
            )

    elif msg_type == 'SYSTEM_TIME':
        return mav.system_time_encode(
            value_of_type('uint64_t', val_type, rng),  
            value_of_type('uint32_t', val_type, rng),  
        )

    elif msg_type == 'PING':
        return mav.ping_encode(
            value_of_type('uint64_t', val_type, rng),  
            value_of_type('uint32_t', val_type, rng),  
            value_of_type('uint8_t', val_type, rng),  
            value_of_type('uint8_t', val_type, rng),  
        )
    
    elif msg_type == 'CHANGE_OPERATOR_CONTROL':
        return mav.change_operator_control_encode(
            value_of_type('uint8_t', val_type, rng),  
            value_of_type('uint8_t', val_type, rng),  
            value_of_type('int', val_type, rng, 0, 255), 
            random_string(25, rng), 
        )

    elif msg_type == 'CHANGE_OPERATOR_CONTROL_ACK':
        return mav.change_operator_control_ack_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'AUTH_KEY':
        return mav.auth_key_encode(
            random_string(32, rng), 
        )

    elif msg_type == 'SET_MODE':
        return mav.set_mode_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
        )

    elif msg_type == 'PARAM_REQUEST_READ':
        return mav.param_request_read_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            random_string(16, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'PARAM_REQUEST_LIST':
        return mav.param_request_list_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'PARAM_VALUE':
        return mav.param_value_encode(
            random_string(16, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'PARAM_SET':
        return mav.param_set_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            random_string(16, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'GPS_RAW_INT':
        return mav.gps_raw_int_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'GPS_STATUS':
        return mav.gps_status_encode(
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(20)],
            [value_of_type('uint8_t', val_type, rng) for _ in range(20)],
            [value_of_type('uint8_t', val_type, rng) for _ in range(20)],
            [value_of_type('uint8_t', val_type, rng) for _ in range(20)],
            [value_of_type('uint8_t', val_type, rng) for _ in range(20)],
        )

    elif msg_type == 'SCALED_IMU':
        return mav.scaled_imu_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'RAW_IMU':
        return mav.raw_imu_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'RAW_PRESSURE':
        return mav.raw_pressure_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'SCALED_PRESSURE':
        return mav.scaled_pressure_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'ATTITUDE':
        return mav.attitude_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'ATTITUDE_QUATERNION':
        return mav.attitude_quaternion_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'LOCAL_POSITION_NED':
        return mav.local_position_ned_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'GLOBAL_POSITION_INT':
        return mav.global_position_int_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'RC_CHANNELS_SCALED':
        return mav.rc_channels_scaled_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'RC_CHANNELS_RAW':
        return mav.rc_channels_raw_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'SERVO_OUTPUT_RAW':
        return mav.servo_output_raw_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_REQUEST_PARTIAL_LIST':
        return mav.mission_request_partial_list_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_WRITE_PARTIAL_LIST':
        return mav.mission_write_partial_list_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_ITEM':
        return mav.mission_item_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'MISSION_REQUEST':
        return mav.mission_request_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_SET_CURRENT':
        return mav.mission_set_current_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_CURRENT':
        return mav.mission_current_encode(
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_REQUEST_LIST':
        return mav.mission_request_list_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_COUNT':
        return mav.mission_count_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_CLEAR_ALL':
        return mav.mission_clear_all_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_ITEM_REACHED':
        return mav.mission_item_reached_encode(
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_ACK':
        return mav.mission_ack_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'SET_GPS_GLOBAL_ORIGIN':
        return mav.set_gps_global_origin_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
        )

    elif msg_type == 'GPS_GLOBAL_ORIGIN':
        return mav.gps_global_origin_encode(
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
        )

    elif msg_type == 'PARAM_MAP_RC':
        return mav.param_map_rc_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            random_string(16, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'MISSION_REQUEST_INT':
        return mav.mission_request_int_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'SAFETY_SET_ALLOWED_AREA':
        return mav.safety_set_allowed_area_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'SAFETY_ALLOWED_AREA':
        return mav.safety_allowed_area_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'ATTITUDE_QUATERNION_COV':
        return mav.attitude_quaternion_cov_encode(
            value_of_type('uint64_t', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(9)],
        )

    elif msg_type == 'NAV_CONTROLLER_OUTPUT':
        return mav.nav_controller_output_encode(
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'GLOBAL_POSITION_INT_COV':
        return mav.global_position_int_cov_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(36)],
        )

    elif msg_type == 'LOCAL_POSITION_NED_COV':
        return mav.local_position_ned_cov_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(45)],
        )

    elif msg_type == 'RC_CHANNELS':
        return mav.rc_channels_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'REQUEST_DATA_STREAM':
        return mav.request_data_stream_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'DATA_STREAM':
        return mav.data_stream_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'MANUAL_CONTROL':
        return mav.manual_control_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'RC_CHANNELS_OVERRIDE':
        return mav.rc_channels_override_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'MISSION_ITEM_INT':
        return mav.mission_item_int_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'VFR_HUD':
        return mav.vfr_hud_encode(
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'COMMAND_INT':
        return mav.command_int_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )
    
    elif msg_type == 'COMMAND_LONG':
        return mav.command_long_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'COMMAND_ACK':
        return mav.command_ack_encode(
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'MANUAL_SETPOINT':
        return mav.manual_setpoint_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng, 0, 1), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'SET_ATTITUDE_TARGET':
        return mav.set_attitude_target_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng, -1, 1), 
        )

    elif msg_type == 'ATTITUDE_TARGET':
        return mav.attitude_target_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng, -1, 1), 
        )

    elif msg_type == 'SET_POSITION_TARGET_LOCAL_NED':
        return mav.set_position_target_local_ned_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'POSITION_TARGET_LOCAL_NED':
        return mav.position_target_local_ned_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'SET_POSITION_TARGET_GLOBAL_INT':
        return mav.set_position_target_global_int_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'POSITION_TARGET_GLOBAL_INT':
        return mav.position_target_global_int_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'LOCAL_POSITION_NED_SYSTEM_GLOBAL_OFFSET':
        return mav.local_position_ned_system_global_offset_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'HIL_STATE':
        return mav.hil_state_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'HIL_CONTROLS':
        return mav.hil_controls_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('float', val_type, rng, 0, 1), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('float', val_type, rng, -1, 1), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'HIL_RC_INPUTS_RAW':
        return mav.hil_rc_inputs_raw_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'HIL_ACTUATOR_CONTROLS':
        return mav.hil_actuator_controls_encode(
            value_of_type('uint64_t', val_type, rng), 
            [value_of_type('float', val_type, rng, -1, 1) for _ in range(16)],
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint64_t', val_type, rng), 
        )

    elif msg_type == 'OPTICAL_FLOW':
        return mav.optical_flow_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'GLOBAL_VISION_POSITION_ESTIMATE':
        return mav.global_vision_position_estimate_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'VISION_POSITION_ESTIMATE':
        return mav.vision_position_estimate_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'VISION_SPEED_ESTIMATE':
        return mav.vision_speed_estimate_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'VICON_POSITION_ESTIMATE':
        return mav.vicon_position_estimate_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'HIGHRES_IMU':
        return mav.highres_imu_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'OPTICAL_FLOW_RAD':
        return mav.optical_flow_rad_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'HIL_SENSOR':
        return mav.hil_sensor_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
        )

    elif msg_type == 'SIM_STATE':
        return mav.sim_state_encode(
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'RADIO_STATUS':
        return mav.radio_status_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'FILE_TRANSFER_PROTOCOL':
        return mav.file_transfer_protocol_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(251)],
        )

    elif msg_type == 'TIMESYNC':
        return mav.timesync_encode(
            value_of_type('int64_t', val_type, rng), 
            value_of_type('int64_t', val_type, rng), 
        )

    elif msg_type == 'CAMERA_TRIGGER':
        return mav.camera_trigger_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
        )

    elif msg_type == 'HIL_GPS':
        return mav.hil_gps_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'HIL_OPTICAL_FLOW':
        return mav.hil_optical_flow_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'HIL_STATE_QUATERNION':
        return mav.hil_state_quaternion_encode(
            value_of_type('uint64_t', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'SCALED_IMU2':
        return mav.scaled_imu2_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'LOG_REQUEST_LIST':
        return mav.log_request_list_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'LOG_ENTRY':
        return mav.log_entry_encode(
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
        )

    elif msg_type == 'LOG_REQUEST_DATA':
        return mav.log_request_data_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
        )

    elif msg_type == 'LOG_DATA':
        return mav.log_data_encode(
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(90)],
        )

    elif msg_type == 'LOG_ERASE':
        return mav.log_erase_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'LOG_REQUEST_END':
        return mav.log_request_end_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'GPS_INJECT_DATA':
        return mav.gps_inject_data_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(110)],
        )

    elif msg_type == 'GPS2_RAW':
        return mav.gps2_raw_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
        )

    elif msg_type == 'POWER_STATUS':
        return mav.power_status_encode(
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'SERIAL_CONTROL':
        return mav.serial_control_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(70)],
        )

    elif msg_type == 'GPS_RTK':
        return mav.gps_rtk_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
        )

    elif msg_type == 'GPS2_RTK':
        return mav.gps2_rtk_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
        )

    elif msg_type == 'SCALED_IMU3':
        return mav.scaled_imu3_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'DATA_TRANSMISSION_HANDSHAKE':
        return mav.data_transmission_handshake_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'ENCAPSULATED_DATA':
        return mav.encapsulated_data_encode(
            value_of_type('uint16_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(253)],
        )

    elif msg_type == 'DISTANCE_SENSOR':
        return mav.distance_sensor_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
        )

    elif msg_type == 'TERRAIN_REQUEST':
        return mav.terrain_request_encode(
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint64_t', val_type, rng), 
        )

    elif msg_type == 'TERRAIN_DATA':
        return mav.terrain_data_encode(
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('int16_t', val_type, rng) for _ in range(16)],
        )

    elif msg_type == 'TERRAIN_CHECK':
        return mav.terrain_check_encode(
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
        )

    elif msg_type == 'TERRAIN_REPORT':
        return mav.terrain_report_encode(
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
        )

    elif msg_type == 'SCALED_PRESSURE2':
        return mav.scaled_pressure2_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'ATT_POS_MOCAP':
        return mav.att_pos_mocap_encode(
            value_of_type('uint64_t', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'SET_ACTUATOR_CONTROL_TARGET':
        return mav.set_actuator_control_target_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('float', val_type, rng, -1, 1) for _ in range(8)],
        )

    elif msg_type == 'ACTUATOR_CONTROL_TARGET':
        return mav.actuator_control_target_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('float', val_type, rng, -1, 1) for _ in range(8)],
        )

    elif msg_type == 'ALTITUDE':
        return mav.altitude_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'RESOURCE_REQUEST':
        return mav.resource_request_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(120)],
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(120)],
        )

    elif msg_type == 'SCALED_PRESSURE3':
        return mav.scaled_pressure3_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
        )

    elif msg_type == 'FOLLOW_TARGET':
        return mav.follow_target_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(3)],            
            [value_of_type('float', val_type, rng) for _ in range(3)],
            [value_of_type('float', val_type, rng) for _ in range(4)],
            [value_of_type('float', val_type, rng) for _ in range(3)],
            [value_of_type('float', val_type, rng) for _ in range(3)],
            value_of_type('uint64_t', val_type, rng), 
        )

    elif msg_type == 'CONTROL_SYSTEM_STATE':
        return mav.control_system_state_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng),             
            [value_of_type('float', val_type, rng) for _ in range(3)],
            [value_of_type('float', val_type, rng) for _ in range(3)],
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )

    elif msg_type == 'BATTERY_STATUS':
        return mav.battery_status_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            [value_of_type('uint16_t', val_type, rng) for _ in range(10)],
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
        )

    elif msg_type == 'AUTOPILOT_VERSION':
        return mav.autopilot_version_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(8)],
            [value_of_type('uint8_t', val_type, rng) for _ in range(8)],
            [value_of_type('uint8_t', val_type, rng) for _ in range(8)],
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint64_t', val_type, rng), 
        )

    elif msg_type == 'LANDING_TARGET':
        return mav.landing_target_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )
    elif msg_type == 'FENCE_STATUS':
        return mav.fence_status_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng),
        )
        
    elif msg_type == 'MAG_CAL_REPORT':
        return mav.mag_cal_report_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng),
        )
        
    elif msg_type == 'EFI_STATUS':
        return mav.efi_status_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 

        )
        
    elif msg_type == 'ESTIMATOR_STATUS':
        return mav.estimator_status_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng),
        )
        
    elif msg_type == 'WIND_COV':
        return mav.wind_cov_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng),
        )
        
    elif msg_type == 'GPS_INPUT':
        return mav.gps_input_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint8_t', val_type, rng),
        )
        
    elif msg_type == 'GPS_RTCM_DATA':
        return mav.gps_rtcm_data_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(180)]
        )
        
    elif msg_type == 'HIGH_LATENCY':
        return mav.high_latency_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng),
        )
        
    elif msg_type == 'HIGH_LATENCY2':
        return mav.high_latency2_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng), 
            value_of_type('int8_t', val_type, rng)
        )
        
    elif msg_type == 'VIBRATION':
        return mav.vibration_encode(
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng)
        )
        
    elif msg_type == 'HOME_POSITION':
        return mav.home_position_encode(
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )
        
    elif msg_type == 'SET_HOME_POSITION':
        return mav.set_home_position_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            [value_of_type('float', val_type, rng) for _ in range(4)],
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
        )
        
    elif msg_type == 'MESSAGE_INTERVAL':
        return mav.message_interval_encode(
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng),
        )
        
    elif msg_type == 'EXTENDED_SYS_STATE':
        return mav.extended_sys_state_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng),
        )
        
    elif msg_type == 'ADSB_VEHICLE':
        return mav.adsb_vehicle_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('int32_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('int16_t', val_type, rng), 
            random_string(9, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng),
        )
        
    elif msg_type == 'COLLISION':
        return mav.collision_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng),
        )
        
    elif msg_type == 'V2_EXTENSION':
        return mav.v2_extension_encode(
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint16_t', val_type, rng), 
            [value_of_type('uint8_t', val_type, rng) for _ in range(249)]
        )
        
    elif msg_type == 'MEMORY_VECT':
        return mav.memory_vect_encode(
            value_of_type('uint16_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            [value_of_type('int8_t', val_type, rng) for _ in range(32)]
        )
        
    elif msg_type == 'DEBUG_VECT':
        return mav.debug_vect_encode(
            random_string(10, rng), 
            value_of_type('uint64_t', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng), 
            value_of_type('float', val_type, rng),
        )
        
    elif msg_type == 'NAMED_VALUE_FLOAT':
        return mav.named_value_float_encode(
            value_of_type('uint32_t', val_type, rng), 
            random_string(10, rng), 
            value_of_type('float', val_type, rng),
        )
        
    elif msg_type == 'NAMED_VALUE_INT':
        return mav.named_value_int_encode(
            value_of_type('uint32_t', val_type, rng), 
            random_string(10, rng), 
            value_of_type('int32_t', val_type, rng),
        )
        
    elif msg_type == 'STATUSTEXT':
        return mav.statustext_encode(
            value_of_type('uint8_t', val_type, rng), 
            random_string(50, rng), 
        )
        
    elif msg_type == 'DEBUG':
        return mav.debug_encode(
            value_of_type('uint32_t', val_type, rng), 
            value_of_type('uint8_t', val_type, rng), 
            value_of_type('float', val_type, rng),
        )
    
    elif msg_type == 'SETUP_SIGNING':
        return mav.setup_signing_encode(
            # 1) which system to target
            value_of_type('uint8_t', val_type, rng),
            # 2) which component on that system
            value_of_type('uint8_t', val_type, rng),
            # 3) the 32-byte secret key
            [value_of_type('uint8_t', val_type, rng) for _ in range(32)],
            # 4) the initial timestamp
            value_of_type('uint64_t', val_type, rng)
        )


    else:
        print(f"Message type {msg_type} not implemented")
        return None

#