from functools import reduce


def get_throughput(data, destination_node, time):
    # data is the list of rows extracted from the .tr file through file_extractor function
    # Calculate the total bytes received through a reduce function.
    # A brief on how the reduce function works: https://docs.python.org/3.0/library/functools.html#functools.reduce
    total_bytes_received = reduce(lambda x, y: x + int(y[5]) if y[3] == destination_node[0:1] and y[0] == "r" else x,
                                  data, 0)
    # Get total bits
    bits = total_bytes_received * 8
    # Get Throughput
    return bits / time


def get_pdr(data, source_node, destination_node):
    # data is the list of rows extracted from the .tr file through file_extractor function
    # source node and destination node would be of the format 4.0. Need to convert it into the format 4
    link_level_source = source_node[0:1]
    link_level_destination = destination_node[0:1]
    # Calculate tht total packets sent by checking the + sign at 0th index and source at 2nd index and destination
    # node at the index 3 from last
    packets_sent = reduce(
        lambda x, y: x + 1 if y[0] == "+" and y[2] == link_level_source and y[-3] == destination_node else x,
        data, 0)
    # Calculate tht total packets received by checking the r sign at 0th index and destination at 3rd index
    packets_received = reduce(
        lambda x, y: x + 1 if y[0] == "r" and y[3] == link_level_destination else x, data, 0)
    # print the source node, destination node, number of packets received and number of packets sent
    print(source_node, destination_node, packets_sent, packets_received)
    return packets_received / packets_sent


def file_extractor(file_name):
    with open(file_name) as f:
        return [line.split() for line in f.readlines()]


if __name__ == '__main__':
    file_name = "/home/alay/PycharmProjects/MC/out50.tr"
    data = file_extractor(file_name)
    n4_throughput = get_throughput(data, "4.0", 4.5)
    n5_throughput = get_throughput(data, "5.0", 4)
    n5_pdr = get_pdr(data, "0.0", "5.0")
    n4_pdr = get_pdr(data, "1.0", "4.0")

    print("Throughput:-\n\tNode 4:", n4_throughput / 1000, "kbps\n\tNode 5:", n5_throughput / 1000, "kbps")
    print("PDR:-\n\tNode 4:", n4_pdr, "\n\tNode 5:", n5_pdr)
