
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('WebAgg')

path = r'D:\Datasets\Electricity'

d1 = pd.read_csv(f'{path}/NEW/nov_dec.csv')
d2 = pd.read_csv(f'{path}/NEW/jan.csv').iloc[:44640, :6]
d3 = pd.read_csv(f'{path}/NEW/feb.csv').iloc[:41760, :6]
d4 = pd.read_csv(f'{path}/NEW/mar.csv').iloc[:, :5]
d5 = pd.read_csv(f'{path}/NEW/apr.csv').iloc[:43200, :5]

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


def cleaner(df):

    mean = df.mean()
    std = df.std()

    for i in range(5):
        for j, v in enumerate(df.iloc[:, i]):
            if j > 0 and j < len(df):        
                if v > mean.iloc[i] + (2 * std.iloc[i]):

                    df.iat[j, i] = (df.iloc[j-1, i] + df.iloc[j+1, i]) / 2
        break

d1 = d1[["date","總耗電量(Kwh)","溫度(C)","濕度(gm3)","總發電量(Kwh)","氫能發電(Kwh)"]]
d2 = d2[["date","總耗電量(Kwh)","溫度(C)","濕度(gm3)","總發電量(Kwh)","氫能發電(Kwh)"]]
d3 = d3[["date","總耗電量(Kwh)","溫度(C)","濕度(gm3)","總發電量(Kwh)","氫能發電(Kwh)"]]
d4 = d4[["date","總耗電量(Kwh)","溫度(C)","濕度(gm3)","總發電量(Kwh)"]]
d5 = d5[["date","總耗電量(Kwh)","溫度(C)","濕度(gm3)","總發電量(Kwh)"]]

date_1 = d1['date']
date_2 = d2['date']
date_3 = d3['date']
date_4 = d4['date']
date_5 = d5['date']

d1 = d1.drop([d1.columns[0], d1.columns[5]], axis = 1).astype(float)
d2 = d2.drop([d2.columns[0], d2.columns[5]], axis = 1).astype(float)
d3 = d3.drop([d3.columns[0], d3.columns[5]], axis = 1).astype(float)
d4 = d4.drop([d4.columns[0]], axis = 1).astype(float)
d5 = d5.drop([d5.columns[0]], axis = 1).astype(float)

cleaner(d1)
cleaner(d2)
cleaner(d3)
cleaner(d4)
cleaner(d5)

d1.iat[36431, 0] = 1.4

all_data = pd.concat([d1, d2, d3, d4, d5])
par_data = pd.concat([d1, d2, d3, d4])#

all_data_dates = pd.concat([date_1, date_2, date_3, date_4, date_5])
par_data_dates = pd.concat([date_1, date_2, date_3, date_4])

all_data.to_csv(f'{path}/all_elec_data.csv', index = False)
par_data.to_csv(f'{path}/par_elec_data.csv', index = False)
# d3.to_csv(f'{path}/feb_elec_data.csv', index = False)

all_data_dates.to_csv(f'{path}/all_elec_dates.csv', index = False)
par_data_dates.to_csv(f'{path}/par_elec_dates.csv', index = False)
# date_3.to_csv(f'{path}/feb_elec_dates.csv', index = False)

# plt.figure(figsize=(64, 8), dpi=160)
# plt.plot(np.arange(len(all_data[30000:50000])), all_data.iloc[30000:50000, 0], label = 'energy_used')
# plt.plot(np.arange(len(all_data[30000:50000])), all_data.iloc[30000:50000, 4], label = 'energy_generated')
# plt.show()

# d3.iat[132968 - offset, 0] = 1.1
# d3.iat[132969 - offset, 0] = 1.1
# d3.iat[171337 - offset, 0] = 1.1
# d3.iat[171338 - offset, 0] = 1.2
# d3.iat[172793 - offset, 0] = 1.3
# d3.iat[173432 - offset, 0] = 1.4

# all_data.iat[36431, 0] = 1.4
# all_data.iat[132968, 0] = 1.1
# all_data.iat[132969, 0] = 1.1
# all_data.iat[171337, 0] = 1.1
# all_data.iat[171338, 0] = 1.2
# all_data.iat[172793, 0] = 1.3
# all_data.iat[173432, 0] = 1.4

# print(data.iloc[173431:173434])

# axis = np.arange(len(data[28000:29000]))
# a = data['氫能發電(Kwh)'][28000:29000]

# axis = np.arange(len(data))
# a = data['總發電量(Kwh)']

# plt.plot(axis, a)
# plt.show()

