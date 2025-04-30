import xml.etree.ElementTree as ET
import sys

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
    lines.append("        uint8_t buf[MAVLINK_MAX_PACKET_LEN];")
    lines.append("        int len = mavlink_msg_to_send_buffer(buf, &msg);")
    lines.append("        for (int ch = 0; ch < MAVLINK_COMM_NUM_BUFFERS; ch++) {")
    lines.append("            mavlink_send_uart_bytes(ch, buf, len);")
    lines.append("        }")
    lines.append("        break;")
    lines.append("    }")
    lines.append("}")

    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path/to/mavlink_definition.xml")
        sys.exit(1)

    xml_file = sys.argv[1]
    c_code = generate_cases(xml_file)
    print(c_code)
