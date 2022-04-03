
from hashlib import new
import pandas as pd
import csv


congress=115

#what file are you grabbing propub cosponsorship data from
cospon_df= pd.read_csv('cosponsors_15.csv')

#create a dictionary using crosswalk
bio_dict={}
with open('bioguide_icpsr_crosswalk.csv',mode='r') as f:
    reader=csv.reader(f)
    bio_dict={rows[1]:rows[2] for rows in reader}


# print(bio_dict)

#create seperate df w just bioguide ids from propub data
cosponsors=cospon_df['cosponsor_bioguide_id']

# print(cosponsors)

new_col=[]
#iterate through propub bioguide IDs and find ICPSR IDs from the crosswalk dictionary
for bioid in cosponsors.iteritems():
    icpsr=bio_dict.get(bioid[1])
    # print(icpsr)
    if icpsr:
        new_col.append(icpsr)
    else:
        new_col.append(' ')

# print(new_col)

#append new column to propublica data
cospon_df=cospon_df.assign(cosponsor_icpsr=new_col)

#create and export to 116_icpsr.csv file
cospon_df.to_csv('116_icpsr.csv')

