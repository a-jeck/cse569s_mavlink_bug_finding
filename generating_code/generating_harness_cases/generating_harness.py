import xml.etree.ElementTree as ET
import sys

# GIVEN THE MAVLINK COMMON MESSAGE DEFINITIONS XML, CREATE A CASE FOR EACH MESSAGE TYPE THAT DECODES IT AND THEN REPACKS IT AND SENDS IT
def generate_cases(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    lines = []
    lines.append("switch (msg.msgid) {")

    for message in root.findall('message'):
        name = message.get('name')
        lower = name.lower()
        lines.append(f"    case MAVLINK_MSG_ID_{name}: {{")
        # Decode
        lines.append(f"        mavlink_{lower}_t payload;")
        lines.append(f"        mavlink_msg_{lower}_decode(&msg, &payload);")
        # Pack fields
        fields = [f.get('name') for f in message.findall('field')]
        args = [f"payload.{fld}" for fld in fields]
        args_str = ', '.join(args)
        lines.append(
            f"        mavlink_msg_{lower}_pack_chan(status.sysid, status.compid, MAVLINK_COMM_0, &msg, {args_str});"
        )
        # Optional send convenience
        lines.append(
            f"        mavlink_msg_{lower}_send(MAVLINK_COMM_0, {', '.join(args)});"
        )
        lines.append("        break;")
        lines.append("    }")

    lines.append("    default: { // generic fallback")
    lines.append("        printf('%s, \"Unsupported message type\n\");")
    lines.append("    }")
    lines.append("}")

    return '\n'.join(lines)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} path/to/mavlink_definition.xml path/to/output.txt")
        sys.exit(1)

    xml_file = sys.argv[1]
    output_file = sys.argv[2]
    c_code = generate_cases(xml_file)

    # Write the generated code to the specified output file
    try:
        with open(output_file, 'w') as f:
            f.write(c_code)
        print(f"Generated C cases written to {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")
        sys.exit(1)
