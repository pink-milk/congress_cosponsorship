
from csv import writer
import time
import json

import requests

#loop through all the bills in this congress, 
# get bill ids, put in list 

headers = {
    'X-API-Key': 'HQmYOCkX2zUhgJUFyMXxSydqAtNcQ5y4WDcDi54b',
}



cosponsors=[]

#which congress you want the bills from
congress='115'

# number of bills introduced in this congress
# manually type in bill counts, if call for a bill that doesn't exist, error message will occur
# could possibly create a try catch to prevent hard code
hr_count=50
hjres_count=0
hconres_count=0

#---------Find Cosponsor Data for Hr-----------------------------------------------------------------------------------------------------------
# loop through bills 1 to hr_count
for bill in range(1,hr_count):
    
    resp = requests.get('https://api.propublica.org/congress/v1/'+str(congress)+'/bills/hr'+str(bill)+'/cosponsors.json', headers=headers)
    resp=resp.json()

    # results=resp
    if resp is None:
        print(str(bill)+ "hr no response")
        continue
    else:
        results=resp.get('results')
        # print(resp)
        if results is None:
            print(str(bill)+ "hr no results in response")
            continue
        else:
            results=results[0]
        


    #pick what info u want from bill
    billdata=[results.get('congress'),
                    results.get('bill_slug'),
                    results.get('sponsor_title'),
                    results.get('sponsor_id'),
                    results.get('sponsor_name'),
                    results.get('sponsor_state')

    ]
    # loop through cosponsers for given bill
    for cospon in results.get('cosponsors'):
        # pick what you want from cosponser data
        cospon_data=[cospon['name'],cospon['cosponsor_id'],cospon['date']]
        #append row to cosponsor data
        cosponsors.append(billdata+cospon_data)

#---------Find Cosponsor Data for Hjres----------------------------------------------------------------------------------------------------------

# loop through bills 1 to hjres_count
for bill in range(1,hjres_count):
    
    resp = requests.get('https://api.propublica.org/congress/v1/'+str(congress)+'/bills/hjres'+str(bill)+'/cosponsors.json', headers=headers)
    resp=resp.json()

    # results=resp
    if resp is None:
        print(str(bill)+ "hjres no response")
        continue
    else:
        results=resp.get('results')
        # print(resp)
        if results is None:
            print(str(bill)+ "hjres no results in response")
            continue
        else:
            results=results[0]
        


    #pick what info u want from bill
    billdata=[results.get('congress'),
                    results.get('bill_slug'),
                    results.get('sponsor_title'),
                    results.get('sponsor_id'),
                    results.get('sponsor_name'),
                    results.get('sponsor_state')

    ]
    # loop through cosponsers for given bill
    for cospon in results.get('cosponsors'):
        # pick what you want from cosponser data
        cospon_data=[cospon['name'],cospon['cosponsor_id'],cospon['date']]
        #append row to cosponsor data
        cosponsors.append(billdata+cospon_data)


#---------Find Cosponsor Data for Hconres-----------------------------------------------------------------------------------------------------------
# loop through bills 1 to hconres_count
for bill in range(1,hconres_count):
    
    resp = requests.get('https://api.propublica.org/congress/v1/'+str(congress)+'/bills/hconres'+str(bill)+'/cosponsors.json', headers=headers)
    resp=resp.json()

    # results=resp
    if resp is None:
        print(str(bill)+ "hconres no response")
        continue
    else:
        results=resp.get('results')
        # print(resp)
        if results is None:
            print(str(bill)+ "hconres no results in response")
            continue
        else:
            results=results[0]
        


    #pick what info u want from bill
    billdata=[results.get('congress'),
                    results.get('bill_slug'),
                    results.get('sponsor_title'),
                    results.get('sponsor_id'),
                    results.get('sponsor_name'),
                    results.get('sponsor_state')

    ]
    # loop through cosponsers for given bill
    for cospon in results.get('cosponsors'):
        # pick what you want from cosponser data
        cospon_data=[cospon['name'],cospon['cosponsor_id'],cospon['date']]
        #append row to cosponsor data
        cosponsors.append(billdata+cospon_data)



    

field_names=['congress','bill_number','sponsor_title','sponsor_bioguide_id','sponsor_name','sponsor_state','cosponsor_name','cosponsor_bioguide_id','date_signed','sponsor_icpsr','cosponsor_icpsr']

#write cosponsorship data to "cosponsors_115.csv"
with open('cosponsors_'+str(congress)+'.csv','w') as f:
    writer = writer(f)
    writer.writerow(field_names)
    writer.writerows(cosponsors)

f.close()





