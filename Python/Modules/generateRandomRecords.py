#https://www.interviewqs.com/ddi-code-snippets/create-df-random-integers

from datetime import datetime
import pandas as pd
import numpy as np

def generateRandomRecords(numRecords, peerRatio, availablePeers, minSize, maxSize):
    # define column names
    cols = ['timeStamp', 'type', 'size', 'duration', 'source_id', 'dest_id']
    # set upper bound for records to create
    idx = range(1, numRecords)

    # init empty dataframe
    resultDf = pd.DataFrame(index=idx ,columns=cols)

    # resultDf = resultDf.astype(
    #     {"timeStamp": object
    #     ,"type": str
    #     ,"size": int
    #     ,"duration": int
    #     ,"source_id": int
    #     ,"dest_id": int
    #     }
    # )

    # assign record type
    # TODO: Use config value for peer ratio
    resultDf['type'] = resultDf.apply(lambda x: str(np.random.choice(['peer', 'origin'], 1, p=[0.8, 0.2])), axis=1)

    # assign source_id
    resultDf['source_id'] = resultDf.apply(lambda x: np.random.randint(1, availablePeers+1), axis=1)


    return resultDf.infer_objects()

