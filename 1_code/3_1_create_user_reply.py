import sys
sys.path.append('/home/milky')

import my_module.module.my_module as mmm

import re
import ast
import string

import numpy as np
import pandas as pd
import networkx as nx

from datetime import datetime

# def foo(G, created_at, tweet_id, user_id, mentioned_users_ids):
#     for mentioned_user_id in mentioned_users_ids:

#         G.add_edge(user_id, mentioned_user_id, count=0, created_at=str(created_at), tweet_id=tweet_id)

def fix_date(datetime_string):
    try:
        return datetime.strptime(datetime_string,'%a %b %d %H:%M:%S +0000 %Y')

    except:
        return np.nan


def fix_ids(id_to_check):
    try:
        return str(int(float(id_to_check)))

    except:
        return np.nan

DATA_PATH = './0_data/user_reply/user_to_user.csv'

dtypes = {'created_at': str,
'tweet_id': str,
'reply_user_id_str': str,
'user_id': str
}

df = pd.read_csv(DATA_PATH, dtype = dtypes, index_col=0) 
print(df.head())

# df.columns = ['created_at', 'tweet_id', 'reply_user_id_str', 'user_id']

# df['created_at'] = df['created_at'].apply(lambda x: fix_date(x))
# df['reply_user_id_str'] = df['reply_user_id_str'].apply(lambda x: fix_ids(x))

print(len(df))
df = df.dropna()
print(len(df))

print(df.head())


# df['mentioned_users_ids'] = df['mentioned_users_ids'].apply(lambda x: ast.literal_eval(x))

# G = nx.MultiDiGraph()

# df.apply(lambda x : foo(G, x['created_at'], x['tweet_id'], x['user_id'], x['mentioned_users_ids']), axis = 1) 

# print(G.number_of_nodes())
# print(G.number_of_edges())

# nx.write_gml(G, "../2_pipeline/user_mentions.gml")
