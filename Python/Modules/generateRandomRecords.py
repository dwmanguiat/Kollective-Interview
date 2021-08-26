#https://www.interviewqs.com/ddi-code-snippets/create-df-random-integers

from ast import Str
from datetime import datetime, timedelta
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import uuid
import datetime

def generateRandomRecords(numRecords, peerRatio, availablePeers, minSize, maxSize):
    # define column names
    cols = ['timeStamp', 'type', 'size', 'duration', 'source_id', 'dest_id']
    # set upper bound for records to create
    idx = range(1, numRecords+1)

    # init empty dataframe
    resultDf = pd.DataFrame(index=idx ,columns=cols).fillna(0)

    # assign record type
    # TODO: Use config value for peer ratio
    resultDf['type'] = resultDf.apply(lambda x: str(np.random.choice(['peer', 'origin'], 1, p=[0.8, 0.2])[0]), axis=1)

    # generate pool of source_id's 
    sourceIDs = []
    for i in range(1, availablePeers):
        sourceIDs.append(uuid.uuid4())

    # assign source_id
    resultDf['source_id'] = resultDf.apply(lambda x: (np.random.choice(sourceIDs) if x['type'] == 'peer' else NaN), axis=1)

    # assign dest_id
    # TODO: prevent source_id = dest_id
    #filterFx = lambda uuid: uuid != 
    resultDf['dest_id'] = resultDf.apply(lambda x: np.random.choice(sourceIDs), axis=1)

    # assign size
    resultDf['size'] = resultDf.apply(lambda x: np.random.randint(minSize, maxSize), axis=1)

    # sequentially assign time stamp
    # times starting from 24 hours ago and incrementing every 5 seconds
    startTime = datetime.datetime.now() - timedelta(days = 1) 
    for i in resultDf.index:
        if i == 1:
            resultDf.at[i, 'timeStamp'] = startTime
        else:
            resultDf.at[i, 'timeStamp'] = resultDf.at[i-1, 'timeStamp'] + timedelta(seconds= 5)

    # resultDf = resultDf.astype(
    #     {"timeStamp": object
    #     ,"type": str
    #     ,"size": int
    #     ,"duration": int
    #     ,"source_id": str
    #     ,"dest_id": int
    #     }
    # )

    return resultDf.infer_objects()

