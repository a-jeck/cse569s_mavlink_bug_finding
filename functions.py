import string, os
from constants import SEED, TYPE_RANGES, MESSAGE_TYPES, MIN, MAX, RAND

def write_message(mav, output_dir, index, msg_type, msg):
    file_path = os.path.join(output_dir, f"seed_{index+1}_{msg_type}.bin")
    with open(file_path, "wb") as f:
        f.write(msg.pack(mav))
    print(f"Saved {msg_type} to {file_path}")


def value_of_type(type_name, val_type, rng, lower=None, upper=None):
    if val_type == RAND:
        return random_value_of_type(type_name, rng, lower, upper)
    # elif val_type == MAX:
        

def random_value_of_type(type_name, rng, lower=None, upper=None):
    """
    Generates a random value given a type name.

    Args:
        type_name (str): The name of the desired data type.

    Returns:
        int: A random value of the specified type.

    Example usage:
    uint64_val = random_value_of_type('uint64_t')

    int8_val = random_value_of_type('int8_t')

    int_0_to_50 = random_value_of_type('int', 0, 50)
    """
  
    if type_name == "float":
        if not lower and not upper:
            return rng.uniform(-3.4028235e38, 3.4028235e38)
        else:
            return rng.uniform(lower, upper)
    
    if type_name == "int":
        if not lower and not upper:
            raise ValueError(f"Int bounds not provided")
        else:
            return rng.randint(lower, upper)

    if type_name not in TYPE_RANGES:
        raise ValueError(f"Unsupported type: {type_name}")

    ctype = TYPE_RANGES[type_name]
    if type_name.startswith('u'):  # Unsigned types
        return rng.randint(0, ctype(-1).value)
    else:
        if type_name == 'int64_t':
            min_val = -2**63
            max_val = 2**63 - 1
        elif type_name == 'int32_t':
            min_val = -2**31
            max_val = 2**31 - 1
        elif type_name == 'int16_t':
            min_val = -2**15
            max_val = 2**15 - 1
        elif type_name == 'int8_t':
            min_val = -2**7
            max_val = 2**7 - 1
        return rng.randint(min_val, max_val)

def random_string(max_length, rng):
    """
    Generates a random string of characters with a maximum length.

    Args:
        max_length (int): The maximum length of the string.

    Returns:
        str: A random string of characters.

    Example usage:
    random_string_40 = random_string(40)
    print(f"Random string (max 40 chars): {random_string_40}")
    """
    if max_length < 0:
        raise ValueError("Maximum length must be non-negative.")

    length = rng.randint(0, max_length)
    characters = string.ascii_letters + string.digits  # Combine letters and digits
    output = ''.join(rng.choice(characters) for _ in range(length))
    return output.encode('ascii')
