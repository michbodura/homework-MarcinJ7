"""
Created on Mon Mar 16

@author: Marcin
"""

from typing import List
from datetime import date
import pandas as pd
from datetime import timedelta

CONFIRMED_CASES_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv '


"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""


confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)

def poland_cases_by_date(day: int, month: int, year: int = 2020):
    data = f'{month}/{day}/{str(year - 2000)}'
    return confirmed_cases.loc[confirmed_cases['Country/Region'] == 'Poland'][f'{data}'].values[0]
    
def top5_countries_by_date(day: int, month: int, year: int = 2020):
    data = f'{month}/{day}/{str(year - 2000)}'
    cases_confirmed = confirmed_cases.groupby('Country/Region').sum()
    return list(cases_confirmed.sort_values(by=[f"{data}"], ascending=False).head(5).index)
    
def no_new_cases_count(day: int, month: int, year: int = 2020):
    #cases_confirmed = confirmed_cases.groupby('Country/Region').sum()
    thisDate = date(year, month, day)
    prevDate = thisDate - timedelta(days = 1)
    thisDateStr = f'{str(thisDate.month)}/{str(thisDate.day)}/{str(thisDate.year - 2000)}'

    prevDateStr = f'{str(prevDate.month)}/{str(prevDate.day)}/{str(prevDate.year - 2000)}'

    casesThisDate = list(confirmed_cases[thisDateStr])
    casesPrevDate = list(confirmed_cases[prevDateStr])

    newCases = 0
    for i,j in zip(casesThisDate, casesPrevDate):
        if(i!=j):
            newCases+=1
            print(confirmed_cases)

    return newCases
    
