# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 07:56:58 2020

@author: FUJITSU
"""
import pandas as pd
df = pd.read_json (r'D:\\Koding\\Python\\Praxis\\twitter_search\\stres\\stres_2020-11-01_to_2020-11-06.json', lines=True)
df.to_csv (r'D:\\Koding\\Python\\Praxis\\twitter_search\\stres\\stres_2020-11-01_to_2020-11-06.csv', index = None)

#tes data csv
import pandas as pd

bantu = pd.read_csv('D:\\Koding\\Python\\Praxis\\twitter_search\\stres\\stres_2020-11-01_to_2020-11-06.csv')
