# congress_cosponsorship
script to get member cosponsorship data for all bills in X congress using propublica congress API. 
additional script to reference bioguide IDs and translate them to ICPSR IDs

It is necessary to get an API key from ProPublica's website before using these scripts [https://www.propublica.org/datastore/api/propublica-congress-api]

propub_congress.py is the main script. instuctions to use are commented within code

bioguide_icpsr_crosswalk.csv is from Josh McCrain [https://congressdata.joshuamccrain.com/messy_data.html] 
and is referenced in 
bioguide_to_icpsr.py, to add additional ICPSR column to propublica data (propublica only uses bioguide IDs)
