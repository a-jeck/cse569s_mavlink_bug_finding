import re
import argparse
import xml.etree.ElementTree as ET


# MESSAGE TYPES NOTSUPPORTED BY PYMAVLINK AT THIS TIME
UNSUPPORTED = ['LINK_NODE_STATUS', 'COMMAND_CANCEL', 'ESC_INFO', 'ESC_STATUS', 'ORBIT_EXECUTION_STATUS', 'TIME_ESTIMATE_TO_TARGETS','ONBOARD_COMPUTER_STATUS', 'COMPONENT_METADATA', 'EVENT', 'CURRENT_EVENT_SEQUENCE', 'REQUEST_EVENT', 'RESPONSE_EVENT_ERROR', ]


# GIVEN AN XML FILE (MAVLINK COMMON MESSAGE DEFINITIONS), EXTRACT ALL DATA TYPES THAT MAKE UP THE MESSAGE (EXCLUDING \EXTENSIONS)
def create_message_switch_code(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    lines = []
    lines.append("def create_message(mav, val_type, rng, msg_type):")

    first = True
    for msg in root.findall('message'):
        name = msg.get('name')
        condition = 'if' if first else 'elif'
        first = False

        func_name = name.lower()

        if name in UNSUPPORTED:
            print(name)
            continue

        args = []
        # Gather fields until an <extensions/> tag is encountered
        for elem in msg:
            if elem.tag == 'extensions':
                break
            if elem.tag != 'field':
                continue
            typ = elem.get('type')
            m = re.match(r"(\w+)\[(\d+)\]", typ)
            if m:
                base, count = m.groups()
                if base == 'char':
                    # Fixed-length string
                    args.append(f"random_string({count}, rng)")
                else:
                    # Array of basic types
                    args.append(f"[value_of_type('{base}', val_type, rng) for _ in range({count})]")
            else:
                # Single basic type
                args.append(f"value_of_type('{typ}', val_type, rng)")

        lines.append(f"    {condition} msg_type == '{name}':")
        lines.append(f"        return mav.{func_name}_encode(")
        for arg in args:
            lines.append(f"            {arg},")
        lines.append("        )")

    lines.append("    else:")
    lines.append("        raise ValueError(f'Unknown message type: {msg_type}')")

    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate switch-case code from XML messages')
    parser.add_argument('xml_file', help='Path to the XML definition file')
    parser.add_argument('output_file', help='Path where the generated code will be written')
    args = parser.parse_args()

    switch_code = create_message_switch_code(args.xml_file)
    # Write the generated switch-case function to the specified output path
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(switch_code)
    print(f"Switch-case code has been written to {args.output_file}")
