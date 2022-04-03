
from csv import writer
import time
import json

import requests

#loop through all the bills in this congress, 
# get bill ids, put in list 

headers = {
    'X-API-Key': 'your_key_here',
}


cosponsors=[]

#which congress you want the bills from
congress='115'

# number of bills introduced in this congress
x=7900

# loop through bills 1 to x
for bill in range(1,x):
    
    resp = requests.get('https://api.propublica.org/congress/v1/'+str(congress)'/bills/hr'+str(bill)+'/cosponsors.json', headers=headers)
    resp=resp.json()

    # results=resp
    if resp is None:
        print(str(bill)+ " no response")
        continue
    else:
        results=resp.get('results')
        print(resp)
        if results is None:
            print(str(bill)+ " no results in response")
            continue
        else:
            results=results[0]
        


    #pick what info u want from bill
    billdata=[results.get('congress'),
                    results.get('bill_slug'),
                    results.get('sponsor_title'),
                    results.get('sponsor_name'),
                    results.get('sponsor_state')

    ]
    # loop through cosponsers for given bill
    for cospon in results.get('cosponsors'):
        # pick what you want from cosponser data
        cospon_data=[cospon['name'],cospon['cosponsor_id'],cospon['date']]
        #append row to cosponsor data
        cosponsors.append(billdata+cospon_data)
    

field_names=['congress','bill_number','sponsor_title','sponsor_name','sponsor_state','cosponsor_name','cosponsor_bioguide_id','date_signed','cosponsor_icpsr']

#write cosponsorship data to "cosponsors_115.csv"
with open('cosponsors_'+str(congress)+'.csv','w') as f:
    writer = writer(f)
    writer.writerow(field_names)
    writer.writerows(cosponsors)

f.close()





