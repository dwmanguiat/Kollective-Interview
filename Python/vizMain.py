from Modules import generateRandomRecords as gr
from Modules import generateVisuals as gv
from Modules import config as cfg

configDict = cfg.config

dataSet =  gr.generateRandomRecords(
    configDict["records"]
    ,configDict["peerRatio"]
    ,configDict["availablePeers"]
    ,configDict["minSize"]
    ,configDict["maxSize"]
    ,configDict["minDuration"]
    ,configDict["maxDuration"]
    )

gv.bandwidthOverTimePlot(dataSet)