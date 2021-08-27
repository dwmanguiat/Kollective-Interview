import matplotlib.pyplot as plt
import pandas as pd
import datetime

def dataSavingPlot(dataIn):

    return

def peerVsOriginDurationPlot(dataIn):

    return 

def bandwidthOverTimePlot(dataIn):
    dataIn = dataIn.set_index(pd.DatetimeIndex(dataIn['timeStamp']))
    print(dataIn.shape)
    dataIn['timeStamp'] = dataIn['timeStamp'].resample('1T').agg({'size':'sum'})
    print(dataIn.shape)
    dataIn.pivot(index="timeStamp", columns="type", values="size").plot.area()
    plt.show()


    return

def generate3PanelPlot(plot1, plot2, plot3):

    return 

