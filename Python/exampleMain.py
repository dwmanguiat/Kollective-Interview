
from Modules import config
from Modules import generateRandomRecords as gr

configDict = config.config

df =  gr.generateRandomRecords(
    configDict["records"]
    ,configDict["peerRatio"]
    ,configDict["availablePeers"]
    ,configDict["minSize"]
    ,configDict["maxSize"]
    ,configDict["minDuration"]
    ,configDict["maxDuration"]
    )

print(df.head())
print(df.shape)
