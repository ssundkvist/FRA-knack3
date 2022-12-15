import networkx as nx
import matplotlib.pyplot as plt

# Python script for FRA knäck 3 2022, "analytikertestet".
# It creates a graph of the network traffic using the source and destination IP addresses included in the caputure.
#
# Before running the script, we need to extract the IP addresses from the captured network traffic.
# We can use TShark with the following command line:
# tshark -r analytikertestet.pcap -T fields -e ip.dst -e ip.src > ./data.txt
# This creates a new file data.txt which the script can use to produce a graph.

# Read the data from the file and return a list of the lines
# Each line represents a source and destination IP address
def data_importer(file_name):
    with open(file_name) as f:
        return f.read().splitlines()

# Create a graph from the data file. Each node is an IP address and each edge is a connection between two IP addresses
def create_ip_graph(file_name):
    # Use multi directional graph
    graph = nx.MultiDiGraph(directed=True)
    for line in data_importer(file_name):
        # Split the line into tokens
        tokens = line.split('\t')
        # Add the nodes to the graph
        graph.add_nodes_from(tokens)
        # Add the edge to the graph
        graph.add_edge(tokens[0], tokens[1])
    return graph

# Display the graph
def display_graph(graph):
    pos=nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    plt.show()

# Run the program
if __name__ == "__main__":
    graph = create_ip_graph("data.txt")
    display_graph(graph)
