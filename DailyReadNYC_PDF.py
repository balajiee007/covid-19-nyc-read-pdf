from tabula import read_pdf
import pandas as pd
from datetime import datetime
from datetime import timedelta
import urllib.request
def main():
    firstdt = datetime.today() + timedelta(days=-1)
    column_names=["SurveyDate","Category","name","value","Percentage"]
    iter_list = []
    yr = str(firstdt.year)
    mnth = str(firstdt.month)
    dt = str(firstdt.day)
    if len(mnth) == 1:
        mnth = '0' + mnth
    if len(dt) == 1:
        dt = '0' + dt
    try:
        url = 'https://www1.nyc.gov/assets/doh/downloads/pdf/imm/' + 'covid-19-daily-data-summary-' + mnth + dt + yr + '-2.pdf'
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
    FinalDf = pd.DataFrame(iter_list, columns=column_names)
    #FinalDf.to_csv('aaa.txt',sep='|', index=False)
    CountyHistDF = pd.read_csv('County_Data.txt', sep='|')
    CountyDF = pd.concat([CountyHistDF,FinalDf[FinalDf['Category'] == 'Borough']])
    CountyDF.to_csv('County_Data.txt', sep='|', index=False)
    # Age Group
    AgeGrpHistDF = pd.read_csv('AgeGrpDF_Data.txt', sep='|')
    AgeGrpDF = pd.concat([AgeGrpHistDF,FinalDf[FinalDf['Category'] == 'Age Group']])
    AgeGrpDF.to_csv('AgeGrpDF_Data.txt', sep='|', index=False)
    # Sex
    SexHistDF = pd.read_csv('SexDF_Data.txt', sep='|')
    SexDF = pd.concat([SexHistDF,FinalDf[FinalDf['Category'] == 'Sex']])
    SexDF.to_csv('SexDF_Data.txt', sep='|', index=False)
    # Total
    TotalHistDF = pd.read_csv('TotalDF_Data.txt', sep='|')
    TotalDF = pd.concat([TotalHistDF,FinalDf[FinalDf['Category'] == 'Total']])
    TotalDF.to_csv('TotalDF_Data.txt', sep='|', index=False)
    # Median Median Age (Range)
    MedianHistDF = pd.read_csv('MedianDF_Data.txt', sep='|')
    MedianDF = pd.concat([MedianHistDF,FinalDf[FinalDf['Category'] == 'Median Age (Range)']])
    MedianDF.to_csv('MedianDF_Data.txt', sep='|', index=False)
    # Deaths
    DeathHistDF = pd.read_csv('DeathsDF_Data.txt', sep='|')
    DeathsDF = pd.concat([DeathHistDF,FinalDf[FinalDf['Category'] == 'Deaths']])
    DeathsDF.to_csv('DeathsDF_Data.txt', sep='|', index=False)
    # Age Group 50 and over
    AgeGrp50HistDF = pd.read_csv('AgeGrp50DF_Data.txt', sep='|')
    AgeGrp50DF = pd.concat([AgeGrp50HistDF,FinalDf[FinalDf['Category'] == 'Age 50 and over']])
    AgeGrp50DF.to_csv('AgeGrp50DF_Data.txt', sep='|', index=False)
main()






