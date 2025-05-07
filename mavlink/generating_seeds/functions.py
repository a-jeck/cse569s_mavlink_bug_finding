import string, os
from constants import SEED, TYPE_RANGES, MESSAGE_TYPES, MIN, MAX, RAND

def write_message(mav, output_dir, index, msg_type, val_type, msg):
    file_path = os.path.join(output_dir, f"seed_{index+1}_{msg_type}_{val_type}.bin")
    with open(file_path, "wb") as f:
        f.write(msg.pack(mav))
    print(f"Saved {msg_type} to {file_path}")


def value_of_type(type_name, val_type, rng, lower=None, upper=None):
    # return random value in valid range
    if val_type == RAND:
        return random_value_of_type(type_name, rng, lower, upper)
    # return max from data type or upper bound
    elif val_type == MAX:
        if type_name in TYPE_RANGES and upper is None:
            range = TYPE_RANGES[type_name]
            return range[MAX]
        elif upper is not None:
            return upper
        else: 
            raise ValueError(f"Bad type and bound passed")

    # return min from data type or lower bound
    elif val_type == MIN:
        if type_name in TYPE_RANGES and lower is None:
            range = TYPE_RANGES[type_name]
            return range[MIN]
        elif lower is not None:
            return lower
        else: 
            raise ValueError(f"Bad type and bound passed")

        

        

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

    
    if lower is not None and upper is not None:
        if (type_name == "int"):
            return rng.randint(lower, upper)
        elif (type_name == "float"):
            return rng.uniform(lower, upper)
        else:
            raise ValueError(f"Unsupported type/bound combination: {type_name}, {lower}, {upper}")
    elif type_name  in TYPE_RANGES:
        range = TYPE_RANGES[type_name]

        if type_name == "float" or type_name == 'double':
            return rng.uniform(range[0], range[1])
        else:
            return rng.randint(range[0], range[1])
    else:
        raise ValueError(f"Unsupported type/bound combination: {type_name}, {lower}, {upper}")

 


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
