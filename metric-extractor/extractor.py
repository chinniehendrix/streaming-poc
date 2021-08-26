import faust
import os
from model import Metric, Order
from filter import filterNoStockOrder
from metric.picker import getPickerItemsPerMinuteMetric

KAFKA_BOOTSTRAP = os.getenv('KAFKA_BOOTSTRAP')

app = faust.App('myapp', broker='kafka://' + KAFKA_BOOTSTRAP, stream_buffer_maxsize=20000)
topic = app.topic('picking-order-finalized-v2', value_type=Order)
sinkTopic = app.topic('amida-picker-metrics', key_type=str, value_type=Metric)

@app.agent(topic)
async def message(messages):
    async for message in messages.filter(filterNoStockOrder):
        metric = getPickerItemsPerMinuteMetric(message.sg)
        if metric != None:
            await sinkTopic.send(value=getPickerItemsPerMinuteMetric(message.sg), key=message.sg.storeId)

if __name__ == "__main__":
    app.main()
