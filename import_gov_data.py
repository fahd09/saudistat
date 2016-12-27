#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:47:04 2016

@author: Home
"""

import pandas as pd
import numpy as np

##################################### 
# Helper methods

def sex_ident(text):
    if text[-1:]=='M':
        return 'Male'
    else:
        return 'Female'

def LF_ident(text):
    if len(text)==3:
        return 'Labor Force'
    else:
        return 'Outside Labor Force'
#####################################


# Work Force by city

fname = 'http://www.stats.gov.sa/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://www.stats.gov.sa/sites/default/files/labour_force_survey_2016_q3ar.xlsx&nid=10099'

# First, read city names (and we have to do that in a separate command)
cities_names = pd.read_excel(fname, 
                     skiprows=4, 
                     skip_footer=5,
                     names = ['cities'],
                     parse_cols=[10])

# read actual data of counts
data = pd.read_excel(fname, 
                     skiprows=7, 
                     skip_footer=5,
                     parse_cols=[1,2,4,5],
                     names=['LFM','LFF','OLFM','OLFF'])

# insert city names in front
data.insert(0, 'city', cities_names)

# convert to long format with city as identifying variable
data_melted = pd.melt(data,  id_vars=['city'])

# now we need to encode sex and labor force status in separate columns
sex=data_melted['variable'].apply(lambda x: str(sex_ident(x)))
lfs=data_melted['variable'].apply(lambda x: str(LF_ident(x)))

# we then need to insert them back into the original long data
data_melted.insert(2, 'sex', sex)
data_melted.insert(3, 'status', lfs)

# drop variable column as we no longer need it
data_melted = data_melted.drop('variable',axis= 1)


data_melted.to_csv('./data/work_force_status_by_gender_by_city.csv')
        
        