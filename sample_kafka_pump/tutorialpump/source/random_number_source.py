import bspump
import random
from datetime import datetime

class RandomNumberSource(bspump.TriggerSource):
    def __init__(self, app, pipeline_id):
        super().__init__(app, pipeline_id)
    async def cycle(self):

        # create a random number between 0 and 100 and timestamp when it was created
        event = {"data": random.randint(0, 100),"timestamp": datetime.now()}
        # convert datetime to string
        event["timestamp"] = event["timestamp"].strftime("%Y-%m-%d %H:%M:%S.%f")

        await self.process(event)
                # print(line)
