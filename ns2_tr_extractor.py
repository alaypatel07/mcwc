from functools import reduce


def get_throughput(data, destination_node, time):
    total_bytes_received = reduce(lambda x, y: x + int(y[5]) if y[-3] == destination_node and y[0] == "r" else x, data,
                                  0)
    bits = total_bytes_received * 8
    return bits / time


def get_pdr(data, source_node, destination_node):
    link_level_source = source_node[0:1]
    packets_sent = reduce(
        lambda x, y: x + 1 if y[0] == "+" and y[2] == link_level_source and y[-3] == destination_node else x,
        data, 0)
    packets_received = reduce(
        lambda x, y: x + 1 if y[0] == "r" and y[-4] == source_node and y[-3] == destination_node else x, data, 0)

    return packets_received / packets_sent


def file_extractor(file_name):
    with open(file_name) as f:
        return [line.split() for line in f.readlines()]


if __name__ == '__main__':
    file_name = "/home/alay/PycharmProjects/MC/AssignmentOut.tr"
    data = file_extractor(file_name)
    n4_throughput = get_throughput(data, "4.0", 3)
    n5_throughput = get_throughput(data, "5.0", 4)
    n4_pdr = get_pdr(data, "0.0", "5.0")
    n5_pdr = get_pdr(data, "1.0", "4.0")

    print("Throughput:-\n\tNode 4:", n4_throughput, "bps\n\tNode 5:", n5_throughput , "bps")
    print("PDR:-\n\tNode 4:", n4_pdr, "\n\tNode 5:", n5_pdr)
