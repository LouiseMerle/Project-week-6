import pandas as pd

terrorism = pd.read_csv('./terrorism/terrorism_total.csv')

terrorism_2016 = terrorism[terrorism.iyear < 2016]

terrorism_regions = terrorism_2016.region_txt.unique()
terrorism_region_subset = terrorism_2016[['iyear', 'success', 'country_txt', 'region_txt']]

terrorism_years = [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
       1981, 1986, 1982, 1983, 1984, 1985, 1987, 1988, 1989, 1990, 1991,
       1992, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
       2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
       2015]


terrorism_dict = {}
i = 0
for region in terrorism_regions:
    mean = (terrorism_region_subset[terrorism_region_subset['region_txt'] == region]['success'].count())/len(terrorism_years)
    for year in terrorism_years:

        current = terrorism_region_subset[(terrorism_region_subset['iyear'] == year) & 
                                (terrorism_region_subset['region_txt'] == region)
                              ]['success']
        if(len(current.values) > 0):
            try:
                current2 = current.astype('int64')
                current_int = current2.count()
            except:
                current_int = 0
        else:
            current_int = 0
        
        if current_int == 0:
            percentage = None
        else:
            percentage = ((current_int - mean)/mean)*100

        sub_dic = {}
        sub_dic['Year'] = year
        sub_dic['region'] = region
        sub_dic['Percentage'] = percentage

        terrorism_dict[i] = sub_dic
        i += 1
    print(region)
    terrorism_increase_1 = pd.DataFrame(terrorism_dict)
    terrorism_increase = terrorism_increase_1.transpose()
    filename = region + '_perc.csv'
    terrorism_increase.to_csv(filename)