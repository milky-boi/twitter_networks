import modin.pandas as pd 
"""
# 1. stupac ID tweeta
# 2. stupac broj lajkova za taj tweet
# 3. stupac broj komentara za taj tweet
# 4. stupac broj retwetanja za taj tweet
# 5. stupac broj quotanja za taj tweet
# 6. stupac broj mentiona za taj tweet
# 7. stupac tekst (to može i u drugi stupac ići, pa se sve pomiče)
"""
print('start')
df = pd.read_csv('/home/milky/infocov/dataset/covid_tweets_by_keyword.csv', index_col=0)
ids = list(df.id_str)
print(len(ids))

df = pd.read_csv('/home/milky/infocov/dataset/all_2020.csv', index_col=0)
rows = df.columns

df = df.loc[df['id_str'].isin(ids)]
print(len(df))


print('preproc done')

df = df[['created_at', 'id', 'id_str', 'retweet_count', 'favorite_count',
  'entities.user_mentions', 'entities.hashtags', 'full_text']]

#'quote_count', 'reply_count',

print(len(df))

with open('/home/milky/infocov/twitter_networks/2_pipeline/1_create_table/out/columns.txt', 'w') as f:
    for row in list(rows):
        f.write(row)
        f.write('\n')
f.close()

df.to_csv('/home/milky/infocov/twitter_networks/2_pipeline/1_create_table/out/table.csv')

df.to_excel('/home/milky/infocov/twitter_networks/2_pipeline/1_create_table/out/table.xlsx')
