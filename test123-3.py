import pandas as pd
import datetime

time_series = pd.read_csv('time_series.csv', low_memory=False)

time_series_70 = time_series[time_series.Year >= 1969]


years = [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,
       1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
       1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
       2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
       2013, 2014, 2015, 2016]
origins = time_series_70['Origin'].unique() 
european = ['Austria', 
       'Belgium',
        'Switzerland',
        'Cyprus',
       'Germany', 'Spain', 'France',
       'United Kingdom', 'Greece',
       'Italy',
       'Netherlands',
       'Sweden',
       'Turkey', 
       'Denmark', 'Norway', 'Portugal', 'Romania',
        'Finland', 'Ireland',
        'Hungary',
        'Iceland', 'Luxembourg', 'Czech Rep.',
       'Poland', 'Albania', 'Armenia',
       'Bulgaria', 'Croatia',
       'The former Yugoslav Republic of Macedonia',
       'Slovenia', 'Bosnia and Herzegovina',
        'Georgia', 'Malta',
       'Russian Federation', 'Slovakia', 
       'Belarus', 'Ukraine',
        'Lithuania', 'Rep. of Moldova', 'Latvia', 'Estonia',
       'Liechtenstein',
       'Montenegro', 'Monaco', 'Serbia and Kosovo']

refugee_dict = {}
i = 0
for land in european:
  for year in years:
    for origin in origins:
      past_year = year - 1
      current = time_series_70[(time_series_70['Year'] == year) & 
                                (time_series_70['Country / territory of asylum/residence'] == land) &
                                (time_series_70['Origin'] == origin) & 
                                ((time_series_70['Population type'] == 'Refugees (incl. refugee-like situations)') |
                                (time_series_70['Population type'] == 'Internally displaced persons') |
                                (time_series_70['Population type'] == 'Asylum-seekers'))
                              ]['Value']
      past = time_series_70[(time_series_70['Year'] == past_year) & 
                                (time_series_70['Country / territory of asylum/residence'] == land) &
                                (time_series_70['Origin'] == origin) & 
                                ((time_series_70['Population type'] == 'Refugees (incl. refugee-like situations)') |
                                (time_series_70['Population type'] == 'Internally displaced persons') |
                                (time_series_70['Population type'] == 'Asylum-seekers'))
                              ]['Value']

      current_int = 0
      past_int = 0

      if(len(current.values) > 0):
        try:
          current2 = current.astype('int64')
          current_int = current2.sum()
        except:
          current_int = 0
      else:
        current_int = 0

      if(len(past.values) > 0):
        try:
          past2 = past.astype('int64')
          past_int = past2.sum()
        except:
          past_int = 0
      else:
        past_int = 0

      sub_dic = {}
      sub_dic['Year'] = year
      sub_dic['Origin'] = origin
      sub_dic['Destination'] = land
      sub_dic['Refugees_increase'] = (current_int - past_int)

      refugee_dict[i] = sub_dic
      i += 1
  print(land)
  refugee_increase_1 = pd.DataFrame(refugee_dict)
  refugee_increase = refugee_increase_1.transpose()
  filename = land + '_sum.csv'
  refugee_increase.to_csv(filename)
