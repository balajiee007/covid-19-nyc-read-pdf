from tabula import read_pdf
import pandas as pd
from datetime import datetime
from datetime import timedelta
import urllib.request
import math
# creating a pdf file object
#covid-19-daily-data-summary-04062020-2.pdf
#https://www1.nyc.gov/assets/doh/downloads/pdf/imm/covid-19-daily-data-summary-04072020-1.pdf
firstdt = datetime.strptime("2020-03-18", '%Y-%m-%d')
column_names=["SurveyDate","Category","name","value","Percentage"]
iter_list = []
while firstdt < datetime.today():
    yr = str(firstdt.year)
    mnth = str(firstdt.month)
    dt = str(firstdt.day)
    if len(mnth) == 1:
        mnth = '0' + mnth
    if len(dt) == 1:
        dt = '0' + dt
    try:
        url = 'https://www1.nyc.gov/assets/doh/downloads/pdf/imm/' + 'covid-19-daily-data-summary-' + mnth + dt + yr + '-2.pdf'
        print(url)
        urllib.request.urlretrieve(url, '/Users/sukumaranb/PycharmProjects/ReadPDF/covid-19-daily-data-summary-' + mnth + dt + yr  + '-2.pdf')
        df = read_pdf('/Users/sukumaranb/PycharmProjects/ReadPDF/covid-19-daily-data-summary-' + mnth + dt + yr + '-2.pdf')
        Category = ""
        dttm = firstdt.strftime('%Y-%m-%d')
        for x in df:
            for item, row in x.iterrows():
                if pd.isnull(row['Total Cases']):
                    Category = str(row['.']).strip()
                elif (row['.'] == "Total") | (row['.'] == "Median Age (Range)") | (row['.'] == "Deaths"):
                    SurveyDate = dttm
                    Cat = str(row['.']).strip()
                    name = str(row['.']).strip()
                    value = str(row['Total Cases']).strip()
                    percentage = ""
                    iter_list.append([SurveyDate,Cat,name,value,percentage])
                else:
                    SurveyDate = dttm
                    name = str(row['.']).replace('-','').strip()
                    value = str(row['Total Cases']).strip().split(" ")[0]
                    percentage = ""
                    try:
                        percentage = str(row['Total Cases']).strip().split(" ")[1][1:].split("%")[0]
                    except:
                        percentage = ""
                    iter_list.append([SurveyDate,Category,name,value,percentage])
    except:
        print("Error")
    firstdt = firstdt + timedelta(days=1)
    #if(dt == "31"):
     #   firstdt = datetime.strptime("2020-04-01",'%Y-%m-%d')
    #else:
     #   firstdt = firstdt + timedelta(days=1)
FinalDf = pd.DataFrame(iter_list, columns=column_names)
FinalDf.to_csv('aaa.txt',sep='|', index=False)






