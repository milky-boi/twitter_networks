
# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet

#! ############################# TO DO ###############################################
#! _  UZ SVE MREZE DODATI TIMESTAMPS NASTAJANJA AKO GA SE IMA
#! _  KREIRATI JOS JEDNU MREZU KOD FOLOWANJA, ALI SE KORISNICI MORAJU PRATITI MEDUSOBNO
#! _  IZVUCI STATISKU HASHTAGOVA 
#! _  IZVUCI STATISTIKU ZA TWEETOVE
#! _ UPLOAD: PODACI ZA MREZU FOLOWANJA  
#TODO: UPLOAD FROM: F:\0_fax\COVID_proj\twiter_scrapper\results
#!
#! ##################################################################################

#* PROGRESS TRACKING
# +------------------+---------+---------+---------+
# | #?NET. TYPE      | PREPROC | DATASET | NETWORK |
# +==================+=========+=========+=========+
# | #* REPLAYANJA    |    X    |    X    |  X, X   | user to user 1826436, tweet to tweet:1796202
# +------------------+---------+---------+---------+
# | #* RETWEETANJA   |    x    |    X    |         | user_to_user: 1246933, tweet to tweet:1246448
# +------------------+---------+---------+---------+
# | #* HASHTAGOVA    |    X    |    X    |         | broj redaka:641899, broj jedinstvenih:118791
# +------------------+---------+---------+---------+
# | #* FOLOWANJA     |    x    |    x    |    x    | (MOZDA NOVI NETWORK)
# +------------------+---------+---------+---------+
# | #* USER MENTIONS |    X    |    X    |    X    | broj redaka:3215615
# +------------------+---------+---------+---------+


#! PODACI ZA MREZE REPLAYANJA
#? UVJET ZA STVARANJE VEZE: KORISTNIK_1 ----SPOMINJE----> KORISNIK_2
# df = df[['id_str', 'user.name', 'entities.user_mentions']]
# df.columns = ['id_str', 'user_name', 'user_mentions']
# print(type(df.user_mentions[1]))
# print(df.user_mentions[1])
# val = df.user_mentions[1][1:-1]
# print(df.user_mentions)

#! PODACI ZA MREZA RETWEETANJA


#? UVJET ZA STVARANJE MREZE: TWEET_2(id)----RETWEETS----> TWEET_1(retweeted_status.id)
# created_at
# id
# id_str
# retweeted_status.created_at
# retweeted_status.id
# retweeted_status.id_str
# retweeted_status.full_text

#! PODACI ZA MREZE HASHTAGOVA
#? AKO SE 2 HASHTAGA POJAVLJUJU SKUPA U TWEETU MEDJU NJIMA SE VEZA STVARA
#? HASHTAG_1 -----POJAVLJIVANJE----- HASHTAG_2

#TODO: PROVJERITI OVE COLUMNSE
#* retweeted_status.entities.hashtags
#* retweeted_status.quoted_status.entities.hashtags
#* quoted_status.entities.hashtags

#! PODACI ZA MREZU FOLOWANJA  
#TODO: UPLOAD FROM: F:\0_fax\COVID_proj\twiter_scrapper\results
#* STVORITI CEMO DVIJE MREZE IZ OVOGA
#* PRVA MREZA:
#? USMJERENA MREZA GDJE SE POVEZUJU KORISNICI NA PRINCIPU
#? KORISNIK_A -------PRATI-------> KORISNIK_B
#* DRUGA MREZA:
#? USMJERENA MREZA GDJE SE POVEZUJU KORISNICI NA PRINCIPU
#? KORISNIK_A -------PRATI-------> KORISNIK_B


#! PODACI ZA MREZU SPOMINJANJA KORISNIKA
#? MREZA NA PRINCIPU
#?KORISNIK_A -----SPOMINJE_U_TWEETU------> KORISNIK_B