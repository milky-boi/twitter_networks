
#%% 
import networkx as nx

GRAPH_PATH = "/home/milky/infocov/twitter_networks/2_pipeline/3_2_create_retweet/user_retweet.gml"

G = nx.read_gml(GRAPH_PATH)

print(G.number_of_nodes())
print(G.number_of_edges())

nodes = list(G.nodes)
in_degree = G.in_degree(nodes)
sorted_d = sorted(in_degree, key=lambda x: x[1], reverse=True)

#%%
sorted_d = sorted_d[:1000]

for i in range(len(sorted_d)):
    node_id, in_degree_value = sorted_d[i]

    print(in_degree_value)
    #list(G.in_degree(node_id)
    #susjedi = list(G.in_degree_iter(node_id))
    susjedi = nx.all_neighbors(G, node_id)

    counter = 0
    while True:
        susjed_id = next(susjedi)
        if G.out_degree(susjed_id) >= 2:
            print('found one')

        # print(G.in_degree(susjed_id))
        # print('-'*10)