from tabula import read_pdf
import pandas as pd
from datetime import datetime
from datetime import timedelta
import urllib.request
column_names=["SurveyDate","Category","name","value","Percentage"]
iter_list = []
try:
    url = 'https://www1.nyc.gov/assets/doh/downloads/pdf/imm/' + 'covid-19-daily-data-summary-' + '03' + '22' + '2020' + '-2.pdf'
    print(url)
    urllib.request.urlretrieve(url,
                               '/Users/sukumaranb/PycharmProjects/ReadPDF/covid-19-daily-data-summary-' + '03' + '22' + '2020' + '-2.pdf')
    df = read_pdf('/Users/sukumaranb/PycharmProjects/ReadPDF/covid-19-daily-data-summary-' + '03' + '22' + '2020' + '-2.pdf')
    Category = ""
    for x in df:
        for item, row in x.iterrows():
            try:
                if pd.isnull(row['10764']):
                    Category = str(row['Total']).strip()
                elif (row['Total'] == "Total") | (row['Total'] == "Median Age (Range)") | (row['Total'] == "Deaths") | (row['Total'] == "Number of Confirmed Cases"):
                    SurveyDate = "2020-03-22"
                    Cat = str(row['Total']).strip()
                    name = str(row['Total']).strip()
                    value = str(row['10764']).strip()
                    percentage = ""
                    iter_list.append([SurveyDate, Cat, name, value, percentage])
                else:
                    SurveyDate = "2020-03-22"
                    name = str(row['Total']).replace('-', '').strip()
                    value = str(row['10764']).strip().split(" ")[0]
                    percentage = ""
                    try:
                        percentage = str(row['10764']).strip().split(" ")[1][1:].split("%")[0]
                    except:
                        percentage = ""
                    iter_list.append([SurveyDate, Category, name, value, percentage])
            except:
                print("Error")#8115
                break
except:
    print("Error")
FinalDf = pd.DataFrame(iter_list, columns=column_names)
FinalDf.to_csv('aaa1.txt',sep='|', index=False)