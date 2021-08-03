import sys
sys.path.append('.')

import pandas as pd
from Classes.Parser import Parser
from Classes.Analytics import Analytics
import datetime
import matplotlib.dates as mdates
import numpy as np
import datetime as dt


import matplotlib.pyplot as plt

if __name__ == '__main__':
    inputfile = './Data/raw/fanta.txt'
    outputfile = './Data/formatted/fanta'
    parser = Parser(inputfile, outputfile)
    parser.parse()
    parser.compute_day_per_user()

    df = parser.df

    date = dt.datetime(2020,8,6)
    df = df[df.date >= date]
    df = df[df.date.dt.hour.isin([21,22,23,0,1,2,3,4,5,6])]

    rems = parser.rems
    adds = parser.adds
    dpu = parser.dpu

    fs=25
    figsize=(15,10)
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]

    analytics = Analytics(df, dpu)

    # mex_per_day = analytics.temporal_evolution_per_day()
    # fig, ax = plt.subplots(figsize=figsize)
    # mex_per_day['message'].plot(ax=ax, rot=45, fontsize=fs)
    # ax.set_xlabel('')
    # ax.set_ylabel('Messages per day', fontsize=fs)
    # ax.grid()
    # fig.show()
    #
    # mpM = analytics.message_per_label('Month', mean=False)
    # fig, ax = plt.subplots(figsize=figsize)
    # mpM['tot'].plot(ax=ax, fontsize=fs)
    # ax.set_xticks(range(1,13))
    # ax.set_xticklabels(months)
    # ax.set_xlabel('')
    # ax.set_ylabel('Average message per month', fontsize=fs)
    # ax.grid()
    # fig.show()
    #
    # mpD = analytics.message_per_label('dow', mean=False)
    # fig, ax = plt.subplots(figsize=figsize)
    # mpD['tot'].plot(ax=ax, fontsize=fs, rot=0)
    # ax.set_xticks(range(0,7))
    # ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    # ax.set_xlabel('')
    # ax.set_ylabel('Average messages per day')
    # ax.grid()
    # fig.show()


    # mph_users = analytics.message_per_label(['Hour'], mean=False)
    # fig, ax = plt.subplots(figsize=figsize)
    # # mph_users['we'].div(len(mph_users['we'])).plot(ax=ax, label='Week Ends', fontsize=fs)
    # # mph_users['wd'].div(len(mph_users['wd'])).plot(ax=ax, label='Week Days', fontsize=fs)
    # mph_users['tot'].div(len(mph_users['tot'])).plot(ax=ax, label='Tot', fontsize=fs)
    # ax.legend(fontsize=fs)
    # ax.set_xticks(range(0,24))
    # ax.set_xlabel('')
    # ax.set_ylabel('Average message per hour')
    # ax.grid()
    # fig.show()

    mpu_norm = analytics.message_per_user(norm=False)
    fig, ax = plt.subplots(figsize=figsize)
    mpu_norm.plot.barh(ax=ax, fontsize=fs)
    ax.grid()
    fig.show()

    # mpu_norm = analytics.message_per_user(norm=True)
    # fig, ax = plt.subplots(figsize=figsize)
    # mpu_norm = mpu_norm[mpu_norm!=np.inf]
    # mpu_norm.plot.barh(ax=ax, fontsize=fs)
    # ax.grid()
    # fig.show()
    #
    # users = mpu_norm.index.tolist()
    # users_activty = analytics.mex_per_day_by_user(bench_mark=None, users=users)
    # users_activty = users_activty
    # fig, ax = plt.subplots(figsize=(15, 10))
    # users_activty.plot(ax=ax, fontsize=20, rot='45')
    # ax.grid()
    # fig.show()





