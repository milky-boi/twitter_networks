
#%% 
import networkx as nx

GRAPH_PATH = "/home/milky/infocov/twitter_networks/2_pipeline/3_2_create_retweet/user_retweet.gml"

G = nx.read_gml(GRAPH_PATH)

print(G.number_of_nodes())
print(G.number_of_edges())


nodes = G.nodes
in_degree = G.in_degree(nodes)[:100]

sorted_d = sorted(in_degree, key=lambda x: x[1], reverse=True)

# sorted_d = sorted_d