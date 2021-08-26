from datetime import datetime

def filterNoStockOrder(message):
    datetimeFormat = '%Y-%m-%dT%H:%M'
    sg = message.sg
    delta = datetime.strptime(sg.metadata.endPicking, datetimeFormat) - datetime.strptime(sg.metadata.startPicking,datetimeFormat)
    return delta.total_seconds() != 0
