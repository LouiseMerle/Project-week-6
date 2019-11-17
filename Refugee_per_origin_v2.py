import pandas as pd
import numpy as np

time_series = pd.read_csv('time_series.csv', low_memory=False)

time_series_70 = time_series[time_series.Year >= 1969]

years = time_series_70['Year'].unique()

origins = time_series_70['Origin'].unique()

total_dic = {}
i = 0
for year in years:
    for origin in origins:
        current = 0
        past = 0
        returned = 0
        past_year = year - 1
        current = time_series_70[(time_series_70['Year'] == year) & 
                                (time_series_70['Origin'] == origin) & 
                                ((time_series_70['Population type'] == 'Refugees (incl. refugee-like situations)') |
                                (time_series_70['Population type'] == 'Internally displaced persons') |
                                (time_series_70['Population type'] == 'Asylum-seekers'))
                              ]['Value']
        
        past = time_series_70[(time_series_70['Year'] == past_year) & 
                                (time_series_70['Origin'] == origin) & 
                                ((time_series_70['Population type'] == 'Refugees (incl. refugee-like situations)') |
                                (time_series_70['Population type'] == 'Internally displaced persons') |
                                (time_series_70['Population type'] == 'Asylum-seekers'))
                              ]['Value']
        current_int = 0
        past_int = 0
        returned_int = 0
        if(len(current.values) > 0):
            try:
                current2 = current.astype(np.int64)
                current_int = current2.sum()
            except:
                current_int = 0
        else:
            current_int = 0

        if(len(past.values) > 0):
            try:
                past2 = past.astype(np.int64)
                past_int = past2.sum()
            except:
                past_int = 0
        else:
            past_int = 0


        sub_dic = {}
        sub_dic['Year'] = year
        sub_dic['Origin'] = origin
        sub_dic['Refugees_increase'] = (current_int - past_int])

        total_dic[i] = sub_dic
        i += 1
        
    print(year)
    country_increase_1 = pd.DataFrame(total_dic)
    country_increase = country_increase_1.transpose()
    filename = str(year) + '_origin.csv'
    country_increase.to_csv(filename)