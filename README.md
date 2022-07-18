# congress_cosponsorship
script to get member cosponsorship data for all bills in X congress using propublica congress API. [https://projects.propublica.org/api-docs/congress-api/]
additional script to reference bioguide IDs and translate them to ICPSR IDs

It is necessary to get an API key from ProPublica's website before using these scripts [https://www.propublica.org/datastore/api/propublica-congress-api]

propub_congress.py is the main script, things to change:
1) add your API key in line 12
2) which congress do you want bills from [117? 116?] line 20
3) how many of each bill? all of them? line 25-27
4) output file name is line 152

Run using: 'python3 propub_congress.py'

bioguide_icpsr_crosswalk.csv is from Josh McCrain [https://congressdata.joshuamccrain.com/messy_data.html] 
and is referenced in 
bioguide_to_icpsr.py, to add additional ICPSR sponsor and cosponsor column to propublica data (propublica only uses bioguide IDs)
1) what is the .csv you're reading from? line 12
2) output file? line 73

Run using: 'python3 bioguide_to_icpsr.py'

This script will take about an hour (or more!) to run through each congress - there's a lot of data, and ProPublica requires a timeout between each call.
