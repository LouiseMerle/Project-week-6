import pandas as pd

total_origin = pd.read_csv('2016_no_destination2.csv')

origins = total_origin.Origin.unique()
years_refugee = [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,
       1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
       1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
       2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
       2013, 2014, 2015, 2016]
percentage_dic = {}
i = 0

for origin in origins:
    mean_refugee = total_origin[total_origin['Origin'] == origin]['Refugees_increase'].mean()
    for year in years_refugee:

        current = total_origin[(total_origin['Year'] == year) & 
                            (total_origin['Origin'] == origin)
                              ]['Refugees_increase']
        
        if(len(current.values) > 0):
            try:
                current_int = int(current.values[0])
            except:
                current_int = 0
        else:
            current_int = 0
            
        if mean_refugee != 0:
            percentage = ((current_int - mean_refugee)/mean_refugee)*100
        else:
            percentage = None

        sub_dic = {}
        sub_dic['Year'] = year
        sub_dic['Origin'] = origin
        sub_dic['Percentage'] = percentage

        percentage_dic[i] = sub_dic
        i += 1
        
    print(origin)
    country_increase_1 = pd.DataFrame(percentage_dic)
    country_increase = country_increase_1.transpose()
    filename = str(year) + '_percentage_no_destination.csv'
    country_increase.to_csv(filename)

