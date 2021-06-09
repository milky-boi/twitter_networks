#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:16:54 2020

@author: ice-cream
"""
from tweepy import OAuthHandler
import tweepy
import  pandas as pd
import json 
import datetime

def connect_to_twitter():
    # Twitter credentials
    consumer_key = ''
    consumer_secret = ''
    access_key = ''
    access_secret = ''
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    print('Twitter API working!')
    
    return api

api = connect_to_twitter()

df = pd.read_csv('profiles_get_tweets.csv')
df['tweets_collectted_at'] = df['tweets_collectted_at'].astype(str)

counter = 1
read_file = 'tweets/collected_tweets_' + str(counter) + '.csv'

for index, row in df.iterrows():
    username = row['Username']
    status_count = row['Statuses']
    collected_bool = row['tweets_collectted_at']
    failed_bool = row['Failed']
     
    if collected_bool == '-1' and failed_bool==False:
        try:
            user_profile = api.get_user(username)
            timeline = user_profile.timeline(count=200, tweet_mode="extended")
    
            df_tweets_on_profile = pd.DataFrame()
            for tweet in timeline:
                json_str = json.dumps(tweet._json, ensure_ascii=False).encode('utf8')
                jtweet = tweet._json
                
                date = jtweet['created_at'][-4:]   
                if date == '2019':
                    df_json = pd.json_normalize(jtweet)
                    df_tweets_on_profile = pd.concat([df_tweets_on_profile, df_json], axis=0)    
            
            try:
                df_all_tweets_found = pd.read_csv(read_file, index_col=0)
                
            except FileNotFoundError: 
                df_all_tweets_found = pd.DataFrame()
                
            if len(df_tweets_on_profile) >= 1:   
                df_all_tweets_found = pd.concat([df_all_tweets_found,df_tweets_on_profile], axis=0)    
                df_all_tweets_found.to_csv(read_file) 
            
            if len(df_all_tweets_found) > 3000:
                counter +=1
                read_file = 'tweets/collected_tweets_18' + str(counter) + '.csv'

            
            df.at[index, 'tweets_collectted_at'] = datetime.datetime.now()
            df.to_csv('profiles_get_tweets.csv')
            
        except tweepy.TweepError:
            with open('failed_users_18.csv', 'a', encoding="utf-8") as outfile:
                outfile.write(str(username)+'\t'+
                          str(status_count)+'\n')
            outfile.close() 
        
        else:
            if status_count >= 200:
                with open('users_more_than_200_18.csv', 'a', encoding="utf-8") as outfile:
                    outfile.write(str(username)+'\t'+
                                  str(status_count)+'\n')
                outfile.close() 
