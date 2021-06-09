import re
import ast
import time
import string

import pandas as pd
import datetime as dt
import networkx as nx
from datetime import datetime
import matplotlib.pyplot as plt 


def check_if_covid_related_text(full_text):
    """
        Returns True if given string contains substring that is related to COVID keywords
        from the list of keywords specified within the function
    """
    lista_keyworda_slobodan = [
        'Capak', 'Beroš', 'Markotić', 'sars-cov2', 'sars-cov-2',
        'SARS-cov2', 'SARS-cov-2', 'SARS-CoV-2', 'SARS-CoV2',
        'Sars-CoV-2', 'Sars-CoV2', 'Sars-cov-2', 'Sars-cov2',
        'korona', 'korone', 'koroni', 'koronom', 'koronu',
        'korona-virus', 'korona-virusi', 'korona-virusom',
        'korona-virusu', 'korona-virusima', 'koronavirus',
        'koronavirusi', 'koronavirusom', 'koronavirusu', 'koronavirusima',
        'koronaviruse', 'corona', 'coronu', 'corone', 'coroni',
        'coronom', 'covid', 'covid19', 'covid-19', 'samoizolacija',
        'samoizolaciju', 'samoizolacije', 'samoizolaciji', 'samoizolacijom',
        'novozaražen', 'novozaražena', 'novozaraženi', 'novozaraženom',
        'novozaražene', 'novozaraženima', 'novozaraženu',
        'pandemija', 'pandemijom', 'pandemiju', 'pandemije', 'pandemiji',
        'epidemija', 'epidemijom', 'epidemiju', 'epidemije', 'epidemiji',
        'epidemiološkim', 'epidemiloške',
        'propusnica', 'propusnice', 'propusnicu', 'propusnicom', 'propusnici',
        'koronakriza', 'koronakrizu', 'koronakrizom', 'koronakrizi', 'koronakrizu', 'koronakrize',
        'cjepivo', 'cjepiva', 'cjepivu', 'cjepivom', 'cjepivima',
        'cijepljenje', 'cijepiti', 'cijepljen', 'procjepljenost',
         'procjepljivanje', 'cijepljenost', 'cijepljena',
        'lockdown', 'stožer', 'stožeru', 'stožerom', 'stožera',
        'propusnica', 'propusnice', 'propusnicu', 'propusnicom', 'propusnicama', 'propusnici'
    ]

    keyword_list_bitne = ['korona', 'virus', 'covid', 'kovid', 'karant', 'izolac', 'ostanidoma',
                        'ostanimodoma', 'slusajstruku', 'slušajstruku', 'ostanimoodgovorni',
                        'corona', 'coronavirus', 'sarscov2', 'sars' 'cov2', 'covid_19',
                        'ncov', '2019-ncov', '2019ncov',  'pfizer', 'moderna', 'koronav',
                        'samoizola', 'viru', 'zaraž', 'zaraz', 'karant', 'izolac', 'epidemiol',
                        'respira', 'testira', 'obolje']

    keyword_list_nebitne = ['stožer', 'dezinf', 'epide', 'pandem', 'odgovorni',
                    'HZJZ', 'infekc', 'inkubacija', 'mask', 'bolnic', 'n95',
                    'doktor', 'ljuskav', 'terapij', 'patoge', 'mjer', 'dijagnost',
                    'obrana ', 'rad od', 'ostanimo', 'doma ', 'kući', 'respir', 'samoizol',
                    'virol', 'distanc', 'zaraz', 'vizir', 'sars', 'who', 'lockd', 'simpto',
                    'Alemka', 'Markoti', 'Vili', 'Beroš', 'Beros', 'Capak', 'prosvjed', 'Šveds',
                    'festival ', 'slobode ', 'ostani', 'struk', 'liječ', 'starač', ' dom ', 'cjep',
                    'nuspoj', 'posljed', 'premin', 'zabilje', 'naciona']

    i = 0
    while i<len(lista_keyworda_slobodan):
        keyword = lista_keyworda_slobodan[i]
        
        try:
            if keyword in full_text:
                return True
        
        except:
            return False

        i += 1

    i = 0

    while i<len(keyword_list_bitne):
        keyword = keyword_list_bitne[i]
        
        try:
            if keyword in full_text:
                return True
        
        except:
            return False

        i += 1

    i = 0
    c = 0 
    while i<len(keyword_list_nebitne):
        keyword = keyword_list_nebitne[i]
        
        try:
            if keyword in full_text:
                c +=1
    
        except:
            return False

        if c >= 2:
            return True

        i += 1

    return False


def calculate_time_differences(pair):
    """
    For a given pair of nodes, the elapsed time is calculated between the activation of the second node,
    after the first has posted a tweet.

    Return list of elpsed times.
    
    """
    diffs = []
    u, v = pair

    a = list(df.loc[df['user_id']==u].created_at.sort_values())
    b = list(df.loc[df['user_id']==v].created_at.sort_values())

    j = 0
    i = 0
    while i < len(a):       
        if i < (len(a)-1):
            # print((b[j] - a[i+1]).total_seconds())

            if (b[j] - a[i+1]).total_seconds() > 0:
                i += 1
                continue

        diff = (b[j] - a[i]).total_seconds()

        if diff > 0:
            diffs.append(diff)
            j += 1
            i += 1
        else:
            j += 1

        if j >= len(b):
            break

    return diffs


def remove_bad_datetimes_from_df():

    # #? DROP BAD DATETIME
    # start_time = time.time()
    # # df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
    # dates = df.created_at
    # index_to_drop = []
    # i = 0
    # for i, date in enumerate(dates):
    #     try:
    #         pd.to_datetime(date, utc=True)
    #     except:
    #         # print(date)
    #         # print(i)
    #         index_to_drop.append(i)
    # df = df.drop(df.index[index_to_drop])
    # print("CONVERT TO DATETIME: %s seconds" % (time.time() - start_time))
    # print(len(index_to_drop))

    pass

def check_foreign(full_text):
    """
        Returns True if given string contains substring that is related to COVID keywords
        from the list of keywords specified within the function
    """
    strane_rjeci = [" c’est ", "c’est", " is ", " are ", " of ", " the ", ' from ',
    ' to be ', ' this ', ' can ', ' for ', ' only ', ' want ', ' Да ', ' српски ', 'Д', 'ш', 'ж']


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