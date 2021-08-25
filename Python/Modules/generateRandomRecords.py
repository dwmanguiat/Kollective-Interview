#https://www.interviewqs.com/ddi-code-snippets/create-df-random-integers

import pandas as pd
import numpy as np

def generateRandomRecords(numRecords, peerRatio, availablePeers, minSize, maxSize):
    resultDf = pd.DataFrame(
        np.random.randint(0, numRecords, int)
        ,columns='test'
    )


    return resultDf

