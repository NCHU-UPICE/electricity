import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

path = r'D:\Datasets\Electricity'

d1 = pd.read_csv(f'{path}/nov_dec.csv')
d2 = pd.read_csv(f'{path}/jan.csv').iloc[:44640, :6]
d3 = pd.read_csv(f'{path}/feb.csv').iloc[:41760, :6]
d4 = pd.read_csv(f'{path}/mar.csv').iloc[:, :5]
d5 = pd.read_csv(f'{path}/apr.csv').iloc[:43200, :5]
d6 = pd.read_csv(f'{path}/may.csv')
d7 = pd.read_csv(f'{path}/jun.csv').iloc[:43200, :5]

d1 = d1.rename(columns = {
    "紀錄時間 " : "date",
    "總耗電量" : "總耗電量(Kwh)",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "氫能發電" : "氫能發電(Kwh)",
    "總發電量" : "總發電量(Kwh)"
})

d2 = d2.rename(columns = {
    "紀錄時間" : "date",
    "總耗電量" : "總耗電量(Kwh)",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "氫能發電" : "氫能發電(Kwh)",
    "太陽能發電" : "總發電量(Kwh)"
})

d3 = d3.rename(columns = {
    "紀錄時間" : "date",
    "總耗電量" : "總耗電量(Kwh)",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "氫能發電" : "氫能發電(Kwh)",
    "太陽能發電度數(kWh)" : "總發電量(Kwh)"
})

d4 = d4.rename(columns = {
    "紀錄時間" : "date",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "總耗電" : "總耗電量(Kwh)",
    "太陽能發電(Kwh)" : "總發電量(Kwh)"
})

d5 = d5.rename(columns = {
    "紀錄時間" : "date",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "總耗電" : "總耗電量(Kwh)",
    "太陽能總發電" : "總發電量(Kwh)"
})

d6 = d6.rename(columns = {
    "紀錄時間" : "date",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "總耗電量" : "總耗電量(Kwh)",
    "太陽能總發電(Kwh)" : "總發電量(Kwh)"
})


d7 = d7.rename(columns = {
    "紀錄時間" : "date",
    "溫度" : "溫度(C)",
    "濕度" : "濕度(gm3)",
    "總耗電量" : "總耗電量(Kwh)",
    "太陽能總發電(Kwh)" : "總發電量(Kwh)"
})

def cleaner(df):

    mean = df.mean(numeric_only = True)
    std = df.std(numeric_only = True)

    for column in df.columns[:4]:

        upper_bound = mean[column] + 3*std[column]
        lower_bound = mean[column] - 3*std[column]

        df[column] = df[column].where(df[column] > lower_bound)
        df[column] = df[column].where(df[column] < upper_bound)

        df[column] = df[column].interpolate(method = 'time')

    return df

def date_formatter(df):

    date = df['date']

    df['month'] = date.str[5:7].astype(int) / 12
    df['day'] = date.str[8:10].astype(int) / 24
    df['hour'] = date.str[-9:-6].astype(int) / 60
    df['minute'] = date.str[-5:-3].astype(int) / 60
    df['second'] = date.str[-2:].astype(int) / 60

    # df = df.drop([df.columns[0]], axis = 1).astype(float)

    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    return df

data = [d1, d2, d3, d4, d5, d6, d7]

for i, datum in enumerate(data):

    df = data[i]
    df = df[["date","總耗電量(Kwh)","溫度(C)","濕度(gm3)","總發電量(Kwh)"]]
    data[i] = cleaner(date_formatter(df))

data = pd.concat(data, axis = 0)

data.to_csv(f'{path}/solar_gen.csv', index = False)