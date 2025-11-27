from collections import namedtuple
from operator import eq, gt, lt
from numpy import prod

with open("day16_input") as f:
    data = f.read()

hex_to_dec = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
    "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"
}

bin_code = "".join([hex_to_dec[x] for x in data])
Packet = namedtuple("Packet", ["version", "ID", "content", "bit_length"])


def get_bin_val(binary):
    return eval(f"0b{binary}")


def read_packet(bin_code):
    version = get_bin_val(bin_code[:3])
    _id = get_bin_val(bin_code[3:6])

    i_start, index_w = 6, 7
    if _id == 4:
        binary = ""

        while True:
            binary += bin_code[i_start + 1: i_start + 5]

            if bin_code[i_start] == "0":
                return Packet(version, _id, get_bin_val(binary), i_start + 5)

            i_start += 5

    else:
        content = []
        type_len = 15 if bin_code[i_start] == "0" else 11
        number_bits = get_bin_val(bin_code[index_w:index_w + type_len])

        if bin_code[i_start] == "0":
            read_bits = 0
            while read_bits != number_bits:
                packet = read_packet(bin_code[index_w + type_len + read_bits:])
                content.append(packet)
                read_bits += packet.bit_length

            return Packet(version, _id, content, index_w + type_len + number_bits)

        elif bin_code[i_start] == "1":
            for _ in range(number_bits):
                packet = read_packet(bin_code[index_w + type_len:])
                content.append(packet)
                index_w += packet.bit_length

            return Packet(version, _id, content, index_w + type_len)


def get_total_version(packet):
    val = packet.version

    if isinstance(packet.content, list):
        val += sum([get_total_version(sub_packet) for sub_packet in packet.content])

    return val


array_ops, compr_ops = {0: sum, 1: prod, 2: min, 3: max}, {5: gt, 6: lt, 7: eq}


def get_total_value(packet):
    if packet.ID == 4:
        return packet.content

    values = [get_total_value(sub_packet) for sub_packet in packet.content]

    if packet.ID in array_ops:
        return array_ops[packet.ID](values)

    if packet.ID in compr_ops:
        return compr_ops[packet.ID](*values)


packet = read_packet(bin_code)
print(f"Part1: {get_total_version(packet)} : 897")
print(f"Part2: {get_total_value(packet)} : 9485076995911")
