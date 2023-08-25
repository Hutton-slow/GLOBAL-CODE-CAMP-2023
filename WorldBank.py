import wbdata
import datetime 
import pandas as pd

data_date = datetime.datetime(2010, 1, 1), datetime.datetime(2011, 1, 1)                                                                                             

#wbdata.get_data("IC.BUS.EASE.XQ", country=["GH"], data_date=data_date)                                                                            

wbdata.get_data("IC.BUS.EASE.XQ", country=["GH"], data_date=data_date) 
wbdata.get_source()
wbdata.get_indicator(source=1)
data=wbdata.search_countries('Ghana')  
wbdata.get_data("IC.BUS.EASE.XQ", country="GH")
wbdata.search_indicators("gdp per capita") 
wbdata.get_incomelevel()   

countries = [i['id'] for i in wbdata.get_country(incomelevel='HIC')]                                                                                                 
indicators = {"IC.BUS.EASE.XQ": "doing_business", "NY.GDP.PCAP.PP.KD": "gdppc"}         
In [13]: df = wbdata.get_dataframe(indicators, country=countries, convert_date=True)
#df.describe()
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True)                                                                                          
df.sort_index().groupby('country').last().corr() 

#CountryName=input("Please enter country name")
#print(data)



#wbdata.get_data("ENF.CONT.COEN.CTAU", country="GH"))
for el in data:
    print(el["country"]["value"])
