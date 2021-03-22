# %%
#%pylab inline
# plot([1,2,3], [3,4,3])

#! IMPROTED PACKAGES 
import pandas as pd 
import datetime
from collections import Counter
from ast import literal_eval
import math
import numpy as np

#! PODACI ZA MREZE REPLAYANJA
#in_reply_to_user_id_str
# id_str
#in_reply_to_status_id_str

# path = '/home/milky/infocov/dataset/all_2020.csv' 
# df = pd.read_csv(path, index_col=0,
#  usecols=['id', 'created_at', 'in_reply_to_status_id_str'])

# df =df.dropna()
# print(len(df))
# df.to_csv('/home/milky/infocov/dataset/user_reply/tweet_to_tweet.csv')


#! PODACI ZA MREZE RETWEETANJA
# path = '/home/milky/infocov/dataset/all_2020.csv' 
#df = pd.read_csv(path, index_col=0, nrows=100)

# usecols=['id', 'created_at',
#  'retweeted_status.id_str', 'retweeted_status.created_at'])
# df = pd.read_csv(path, index_col=0, usecols=['id', 'created_at',
# 'user.id_str', 'retweeted_status.created_at', 'retweeted_status.id_str'])
# df =df.dropna()
# print(len(df))
# df.to_csv('/home/milky/infocov/dataset/user_retweet/user_to_user.csv')



# df = pd.read_csv(path, index_col=0, usecols=['id', 'created_at',
# 'user.id_str', 'retweeted_status.created_at', 'retweeted_status.user.id_str'])
# df =df.dropna()
# print(len(df))
# df.to_csv('/home/milky/infocov/dataset/user_retweet/user_to_user.csv')
# # retweeted_status.user.id_str


# id_str
# retweeted_status.id_str

# user.screen_name
#nema screen namea svih pa mozda pomocu retweeted_status.user.id_str 
#pronaci user screen_name







#! PODACI ZA MREZE HASHTAGOVA
# path = '/home/milky/infocov/dataset/original_2020.csv' 
# df = pd.read_csv(path, index_col=0,
#  usecols=['id', 'created_at', 'user.id_str', 'entities.hashtags'])

# #df = df[['id', 'created_at', 'user.id_str', 'entities.user_mentions']]
# df = df.dropna()

# def get_mentioned_user_info(input_string):
#     users_mentioned = []

#     try:
#         l = eval(input_string)
#     except:
#         return np.nan

#     try:
#         for elem in l:
#             try:
#                 d = eval(str(elem))

#                 users_mentioned.append(d['text'])
#             except [KeyError, NameError]:
#                 return np.nan

#     except TypeError:
#         return np.nan

#     if len(users_mentioned) == 0:
#         return np.nan

#     else:
#         return users_mentioned

# df['mentioned_hashtags'] = df['entities.hashtags'].map(lambda x: get_mentioned_user_info(x))
# df = df.drop(columns=['entities.hashtags'])

# print(len(df))
# print('number of bad rows:', str(df['mentioned_hashtags'].isna().sum()))
# df = df.dropna()
# print(len(df))
# df.to_csv('/home/milky/infocov/dataset/hashtags/all_hashtags_2020.csv')

#     for ele in converted_list:
#         all_hashtags.append(ele.replace("\'", ''))

# all_hashtags = pd.Series(all_hashtags)
# all_hashtags = all_hashtags.value_counts()
# all_hashtags.to_csv('/home/milky/infocov/dataset/hashtags/all_hashtags_counts_2020.csv')

# %%
#! PODACI ZA MREZU SPOMINJANJA KORISNIKA

# path = '/home/milky/infocov/dataset/original_2020.csv' 
# df = pd.read_csv(path, index_col=0,
#  usecols=['id', 'created_at', 'user.id_str', 'entities.user_mentions'])

# #df = df[['id', 'created_at', 'user.id_str', 'entities.user_mentions']]
# df = df.dropna()

# def get_mentioned_user_info(input_string):
#     users_mentioned = []
#     try:
#         l = eval(input_string)
#     except:
#         return np.nan

#     try:
#         for elem in l:
#             try:
#                 d = eval(str(elem))

#                 users_mentioned.append(d['id_str'])
#             except [KeyError, NameError]:
#                 return np.nan

#     except TypeError:
#         return np.nan

#     if len(users_mentioned) == 0:
#         return np.nan

#     else:
#         return users_mentioned

# df['mentioned_users_ids'] = df['entities.user_mentions'].map(lambda x: get_mentioned_user_info(x))
# df = df.drop(columns=['entities.user_mentions'])

# print(len(df))

# print('number of bad rows:', str(df['mentioned_users_ids'].isna().sum()))
# df = df.dropna()
# print(len(df))
# df.to_csv('/home/milky/infocov/dataset/user_mentions/user_mentions.csv')



#! CREATE NETWORKS 

import ast
import networkx as nx 

def add_nodes_from_list_to_graph(G, node_list):
    
    for node in node_list:
        if node not in G:
            G.add_node(node)

    for i in range(len(node_list)):
        node_1 = node_list[i]

        for j in range(len(node_list)):
            if i<j:
                node_2 = node_list[j]

                if G.has_edge(node_1, node_2):
                    G[node_1][node_2]['count'] +=1

                else:
                    G.add_edge(node_1, node_2, count=1)

df = pd.read_csv('/home/milky/infocov/dataset/hashtags/all_hashtags_2020.csv', index_col=0)
hashtags = df.mentioned_hashtags

G = nx.Graph()

for row in hashtags:
    converted_list = row.strip('][').split(', ')
    if len(converted_list) > 1:
        add_nodes_from_list_to_graph(G, converted_list)

name = '/home/milky/infocov/created_networks/hashtag_hashtag.gml'
nx.write_gml(G, name)





