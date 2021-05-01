#import pandas as pd

import requests
import json
url="https://api.covid19india.org/state_district_wise.json"
response=requests.get(url).text
response_info=json.loads(response)
for state, state_data in response_info.items():
    district_info =state_data['districtData']
    for district_name,district_values in district_info.items():        
        print(state,district_name,district_values['active'],district_values['confirmed'],district_values['deceased'],district_values['recovered'])
        




#covid_data= pd.DataFrame(data=response_info.items(), columns=['StateName','District'])#,'Active','Confirmed','Deciesed','Removed'])
#covid_data.head(10)   
#print(covid_data)