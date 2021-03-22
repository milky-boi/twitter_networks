import modin.pandas as pd 


df = pd.read_csv('/home/milky/infocov/dataset/all_2020.csv',
 nrows=1000, index_col=0)

df = df.drop(df.columns[0], axis=1)

df.to_csv('/home/milky/infocov/twitter_networks/2_pipeline/0_load_data/out/df_2020_sample.csv')




