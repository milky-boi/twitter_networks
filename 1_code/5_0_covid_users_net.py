#%%
#? IMPORTI PAKETA
import sys
sys.path.append('/home/milky')
import my_module.module.my_module as mmm

import help_foos as hf

import re
import ast
import time
import string

import pandas as pd
import datetime as dt
import networkx as nx
from datetime import datetime
import matplotlib.pyplot as plt 

#%%
#? IMPORT PODATAKA
start_time = time.time()

# DATA_PATH = '/home/milky/infocov/dataset/user_mentions/user_mentions.csv'
DATA_PATH = '/home/milky/infocov/dataset/original_2020_clear.csv'

dtypes = {'created_at': str,
'id': str,
'full_text': str,
'user.id_str': str,
'user.screen_name': str,
'entities.hashtags': str,
'entities.user_mentions': str}

fields = ['created_at', 'id', 'full_text', 'user.id_str', 'user.screen_name',
'entities.hashtags',  'entities.user_mentions']

df = pd.read_csv(DATA_PATH, dtype=dtypes, usecols=fields)

df = df[df['full_text'].notna()]

print(len(df))
print("DATA IMPORT: %s seconds" % (time.time() - start_time))

# df = df.head(20)

#%%
#? CONVERT DATETIME
def check_foreign(full_text):
    """
        Returns True if given string contains substring that is related to COVID keywords
        from the list of keywords specified within the function
    """
    strane_rjeci = [" c’est ", "c’est", " is ", " are ", " of ", " the ", ' from ',
    ' to be ', ' this ', ' can ', ' for ', ' only ', ' want ', ' Да ', ' српски ', 'Д', 'ш', 'ж',
    'جججمل_مدينه_بر' ,'ايكفقير' ,'حظ' ,'وهمومي' ,'تهد' ,'الحيل' ,'،' ,'اسلي' ,' نفسي ',
    ' just ', ' because ']


    i = 0
    while i<len(strane_rjeci):
        keyword = strane_rjeci[i]
        
        try:
            if keyword in full_text:
                return True
        
        except:
            return False

        i += 1

    return False


start_time = time.time()

#df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
# df['created_at'] = df['created_at'].apply(lambda x: x.isoformat())

df['strane_rijeci'] = df['full_text'].apply(lambda x: check_foreign(x))

print("number of STRANE tweets:" + str(df['strane_rijeci'].value_counts()))

df_c = df.loc[~df['strane_rijeci']]
#%%
s = df_c.sample(1000)[['full_text']]

#print("CONVERT TO DATETIME: %s seconds" % (time.time() - start_time))
#%%
#? FILTER ZA VREMENSKI INTERVAL

# dtypes = {'created_at': str,
# 'tweet_id': str,
# 'full_text': str,
# 'user_id': str,
# 'user_screen_name': str}

# DATA_PATH = '/home/milky/infocov/dataset/original_2020_11mj.csv'
# df = pd.read_csv(DATA_PATH, index_col=0, dtype = dtypes)

# df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
# start_time = time.time()
# mask = (df['created_at'] >= '2020-11-01 00:00:00') & (df['created_at'] <= '2020-11-30 23:59:59')
# df = df.loc[mask]

# DATA_PATH = '/home/milky/infocov/dataset/original_2020_11mj.csv'
# df.to_csv(DATA_PATH)
# # df['mentioned_users_ids'] = df['mentioned_users_ids'].apply(lambda x: ast.literal_eval(x))
# # df['mentioned_users_usernames'] = df['mentioned_users_usernames'].apply(lambda x: ast.literal_eval(x))

# print("TIME INTERVAL FILTER: %s seconds" % (time.time() - start_time))

#%%
# #? RANDOM SAMPLE NODES
# df = df.sample(n = 21255, random_state=2)
# selected_nodes = list(set(df.user_id))
#%%



#%%
#? RONA TVITS FILTER

start_time = time.time()

df['rona_related'] = df['full_text'].apply(lambda x: hf.check_if_covid_related_text(x))
print("number of COVID tweets:" + str(df['rona_related'].value_counts()))
df = df.loc[df['rona_related']]

print("RONA TVITS FILTER: %s seconds" % (time.time() - start_time))

#%%
#? GRAF DIO
start_time = time.time()
df = df.dropna()
selected_nodes=list(set(df.user_id))
print(len(selected_nodes))
selected_nodes = [str(int(x)) for x in selected_nodes]
print(selected_nodes[0])

path = r"/home/milky/infocov/dataset/users_following.gml"
G = nx.read_gml(path)
print("number of nodes in graph " + str(G.number_of_nodes()))
print("number of edges in graph " + str(G.number_of_edges()))

lista_cvorova = list(G.nodes)

H = G.subgraph(selected_nodes)
print("number of nodes in subgraph " + str(H.number_of_nodes()))
print("number of edges in subgraph " + str(H.number_of_edges()))

print("TAKE SUBGRAPH FROM GRAPH: %s seconds" % (time.time() - start_time))

#%%
#? PALJENJE CVOROVA
start_time = time.time()

df['user_id'] = df['user_id'].apply(lambda x: str(int(x)))

pairs = [(u, v) for u, v in list(H.edges)]

import multiprocessing
with multiprocessing.Pool(50) as pool:
    all_diffs = list([ diff_list for diff_list in pool.map(hf.calculate_time_differences, pairs) ])

print("PALJENJE CVOROVA: %s seconds" % (time.time() - start_time))


#%%
all_diffs_no_covid = all_diffs

#%%
from matplotlib import pyplot
import numpy 

x = all_diffs_covid
y = all_diffs_no_covid

bins = numpy.linspace(-10, 10, 100)


pyplot.hist(x, bins=50, alpha=0.5, label='covid')
pyplot.hist(y, bins=50, alpha=0.5, label='no covid')
pyplot.legend(loc='upper right')

pyplot.xscale("log")
pyplot.yscale("log")

# plt.axvline(x=3600, c='r')
pyplot.axvline(x=86400, c='r') 
week_num = 86400*7
pyplot.axvline(x=week_num, c='r') 
 
pyplot.xlim([0, 86400*30])
pyplot.ylim([0, 10**7])

pyplot.show()


#%%
#? PLOT HISTOGRAM VREMENA PALJENJA
import itertools
covid_tweets_trig_list = list(itertools.chain.from_iterable(all_diffs))

plt.title('RANDOM 11. mj tvitovi u mrezi')
# plt.xscale("log")
plt.yscale("log")
plt.hist(covid_tweets_trig_list, bins=50)

# plt.axvline(x=3600, c='r')

plt.axvline(x=86400, c='r') 

week_num = 86400*7
plt.axvline(x=week_num, c='r') 
 
plt.xlim([0, 86400*30])
plt.ylim([0, 10**7])


#%%
# #? BROJANJE VREMENA IZMEDJU TVITOVA
times = []
list_tweets = list(df.created_at.sort_values())
i = 0 
j = 1

while j<len(list_tweets):
    first = list_tweets[i]
    second = list_tweets[j]

    diff = (second - first).total_seconds()
    times.append(diff)

    i += 1
    j += 1

plt.title("SVI tvitovi BEZ mreze")
plt.xscale("log")
plt.yscale("log")
plt.hist(times, bins=50)
plt.xlim([0, 1200])
plt.ylim([0, 10**7])

#%%
import matplotlib.pyplot as plt 
plt.xscale("log")
plt.yscale("log")
plt.hist(times, bins=50)
plt.xlim([0, 3000000])
plt.ylim([0, 10**7])


# #%%
# #? FILTER ZA KORONA TVITOVE

# df['rona_related'] = df['full_text'].apply(lambda x: rona_check(x))
# print(df['rona_related'].value_counts())
# df = df.loc[~df['rona_related']]


# #%%

# df = df[['created_at', 'tweet_id', 'user_id', 'user_screen_name']]
# #%%
# #? FILTER ZA CVOROVE IZ MREZE KOJI SU TVITALI U ZADANOM DATASETU

# selected_nodes=set(list(df.user_id))
# print(len(selected_nodes))

# import networkx as nx 

# path = r"/home/milky/infocov/dataset/users_following.gml"
# G = nx.read_gml(path)

# print(G.number_of_nodes())

# H = G.subgraph(selected_nodes)
# print(H.number_of_nodes())
# print(H.number_of_edges())

# #%%
# #? ALGORITAM ZA MJERENJE VREMENA PALJENJA IZMEDJU POVEZANIH CVOROVA
# import datetime as dt

# def time_diffs(a, b):
#     diffs = []
#     j = 0
#     i = 0
#     while i < len(a):       
#         if i < (len(a)-1):
#             # print((b[j] - a[i+1]).total_seconds())

#             if (b[j] - a[i+1]).total_seconds() > 0:
#                 i += 1
#                 continue

#         diff = (b[j] - a[i]).total_seconds()

#         if diff > 0:
#             diffs.append(diff)
#             j += 1
#             i += 1
#         else:
#             j += 1

#         if j >= len(b):
#             break

#     return diffs

# res = []
# for edge in list(H.edges()):
#     u, v = edge

#     node_list1 = list(df.loc[df['user_id']==u].created_at.sort_values())
#     node_list2 = list(df.loc[df['user_id']==v].created_at.sort_values())

#     t = time_diffs(node_list1, node_list2)
    
#     res = res + t 
#     # if len(t) > 1:
#     #     break

# #%% 
# #? PLOT RJESENJA, HISTOGRAM

# import matplotlib.pyplot as plt 


# plt.yscale("log")
# plt.hist(res, bins=50)
# plt.xlim([0, 3000000])
# plt.ylim([0, 10**7])

# #%%

# # for activation_time_n1 in node_list2:
# #     time_delta = activation_time_n2 - activation_time_n1 


# # node1 --> node2

# # node1_list = df.select where user id = node1_id  
# # node2_list = df.select where user id = node2_id  

# # take first in node1_list
# #     find closest in node2list

# #     return diff


# #%%
# def extract_day(datetime_str):
#     day = datetime_str[8:10]
#     return int(day)

# statuses = df[['created_at', 'user_id']]
# statuses['created_at'] = statuses['created_at'].apply(lambda x: extract_day(x))

# #%%
# statuses = statuses.sort_values('created_at')

# def return_status(i, x):
#     x = int(x)
#     i = int(i)

#     if i == x:
#         return 1

#     else:
#         return 0
        
# for i in range(14,30):
#     statuses[i] = statuses['created_at'].apply(lambda x: return_status(i, x))

# #%%
# statuses = statuses.drop_duplicates(subset=['user_id'], keep='first')

# d = {}
# for index, row in statuses.iterrows():
#     row = list(row)
#     created_at = row[0]
#     user_id = row[1]
#     stats= row[2:]

#     value = 0
#     for i in range(len(stats)):
#         if stats[i] < 1 and value == 0:
#             pass

#         elif stats[i] == 1:
#             value = 2

#         elif value == 2:
#             stats[i] = 1

#     d.update({str(user_id): stats})
            
# #%%
# for key, value in d.items():
#     print(key)


#              #%%
# # nx.write_gml(H, "subgr.gml")
# node_info = df[['user_id', 'user_screen_name']]
# node_info = node_info.drop_duplicates(subset=['user_screen_name'], keep='first')

# for inex, row in node_info.iterrows():
#     user_id, user_screen_name = row
#     try:
#         H.nodes[user_id]['scree_name']=user_screen_name

#     except:
#         pass

# # nx.write_gml(H, "subgr.gml")

    
