import matplotlib.pyplot as plt
import pandas as pd
import datetime

def dataSavingPlot(dataIn):
    #aggregate sum by type
    aggData = dataIn[['type', 'size']].groupby(['type']).sum()

    #calculate savings %
    ratio = (dict(aggData)['size']['peer']/aggData['size'].sum())
    aggData.plot.pie(y='size', title='{:.2%} Bandwidth Savings'.format(ratio))
    plt.show()

    return 

def peerVsOriginDurationPlot(dataIn):
    aggData = dataIn[['type', 'duration']].groupby(['type']).sum()
    aggData.plot.bar(y='duration', title='Transfer Durations (s)')
    plt.show()

    return 

def bandwidthOverTimePlot(dataIn):
    dataIn = dataIn[['timeStamp', 'type', 'size']]

    dataPeer = dataIn[dataIn['type'] == 'peer']
    dataOrigin = dataIn[dataIn['type'] == 'origin']

    dataPeer['cumSize'] = dataPeer['size'].cumsum()
    dataOrigin['cumSize'] = dataOrigin['size'].cumsum()

    dataCombo = dataPeer.append(dataOrigin)

    dataPivot = dataCombo.pivot(index='timeStamp', columns='type', values='cumSize')

    dataPivot.plot(style='.-', title='Cumulative Bandwidth Consumption Over Time')
    plt.show()

    return


