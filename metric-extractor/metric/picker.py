from datetime import datetime
from model import Metric, Label
import json

def computeItemCountPerMinute(sg):
    datetimeFormat = '%Y-%m-%dT%H:%M'
    delta = datetime.strptime(sg.metadata.endPicking, datetimeFormat) - datetime.strptime(sg.metadata.startPicking,datetimeFormat)
    return sg.metadata.pickedUnitsCount/(delta.total_seconds()/60)

def getPickerItemsPerMinuteMetric(sg):
    datetimeFormat = '%Y-%m-%dT%H:%M:%S.%fZ'
    name = f'picker_items_per_minute:{sg.pickerId}:{sg.storeId}'
    value = computeItemCountPerMinute(sg)
    unixTimestamp = int(datetime.strptime(sg.updatedAt, datetimeFormat).strftime("%s"))*1000
    labels = [
        Label(key="pickerId", value=sg.pickerId),
        Label(key="storeId", value=sg.storeId)
    ]
    return Metric(name=name, value=value, unixTimestamp=unixTimestamp, labels=labels)
