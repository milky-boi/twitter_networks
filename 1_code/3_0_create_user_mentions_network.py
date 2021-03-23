import sys
sys.path.append('/home/milky')

import my_module.module.my_module as mmm

import re
import ast
import string

import pandas as pd
import networkx as nx

from datetime import datetime

def foo(G, created_at, tweet_id, user_id, mentioned_users_ids):
    for mentioned_user_id in mentioned_users_ids:

        G.add_edge(user_id, mentioned_user_id, created_at=str(created_at), tweet_id=tweet_id)


DATA_PATH = './0_data/user_mentions/user_mentions.csv'

dtypes = {'created_at': str,
'id': str,
'user.id_str': str,
'mentioned_users_ids': str}

df = pd.read_csv(DATA_PATH, dtype = dtypes)
print(df.head(5))

df.columns = ['created_at', 'tweet_id', 'user_id', 'mentioned_users_ids']
df['created_at'] = df['created_at'].apply(lambda x: datetime.strptime(x,'%a %b %d %H:%M:%S +0000 %Y'))

df['mentioned_users_ids'] = df['mentioned_users_ids'].apply(lambda x: ast.literal_eval(x))

G = nx.MultiDiGraph()

df.apply(lambda x : foo(G, x['created_at'], x['tweet_id'], x['user_id'], x['mentioned_users_ids']), axis = 1) 

print(G.number_of_nodes())
print(G.number_of_edges())

nx.write_gml(G, "/home/milky/infocov/twitter_networks/2_pipeline/3_0_create_user_mentions_network/user_mentions.gml")
