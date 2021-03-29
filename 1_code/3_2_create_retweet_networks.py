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

['rt_created_at', 'rt_id', 'rt_user_id',
 'ot_creation_time', 'ot_id', 'ot_user_id']
 
def create_network(G, row):
    row['created_at']
    row['rt_id']

    u = row['ot_user_id']
    v = row['user_id']
    
    row['ot_creation_time']
    
    G.add_node( )
    G.add_edge(user_id, reply_user_id_str, created_at=str(created_at), tweet_id=tweet_id)

dtypes = {'created_at': str,
'id': str,
'user.id_str': str,
'retweeted_status.created_at': str,
'retweeted_status.id_str': str,
'retweeted_status.user.id_str': str}

#DATA_PATH = './0_data/user_reply/user_to_user.csv'
DATA_PATH = '/home/milky/infocov/dataset/user_retweet/tweet_to_tweet.csv'
df = pd.read_csv(DATA_PATH, dtype = dtypes) 

df.columns = ['rt_created_at', 'rt_id', 'rt_user_id',
 'ot_creation_time', 'ot_id', 'ot_user_id']

df['rt_created_at'] = df['rt_created_at'].apply(lambda x: fix_date(x))
df['ot_creation_time'] = df['ot_creation_time'].apply(lambda x: fix_date(x))

df['rt_id'] = df['rt_id'].apply(lambda x: fix_ids(x))
df['ot_id'] = df['ot_id'].apply(lambda x: fix_ids(x))

G = nx.DiGraph()
df = df.dropna()

df.apply(lambda row : create_network(G, row), axis = 1) 

# print(G.number_of_nodes())
# print(G.number_of_edges())

# nx.write_gml(G, "/home/milky/infocov/twitter_networks/2_pipeline/3_2_create_user_retweet/user_retweet.gml")
