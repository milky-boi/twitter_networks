import networkx as nx

GRAPH_PATH = "/home/milky/infocov/twitter_networks/2_pipeline/3_1_create_user_reply/user_reply_tweet_to_tweet.gml"

G = nx.read_gml(GRAPH_PATH)

print(G.number_of_nodes())
print(G.number_of_edges())