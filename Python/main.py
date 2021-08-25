
from Modules import config
from Modules import generateRandomRecords

configDict = config
print(
    generateRandomRecords(
    configDict["records"]
    ,config["peerRatio"]
    ,config["availablePeers"]
    ,config["minSize"]
    ,config["maxSize"]
    ).head())