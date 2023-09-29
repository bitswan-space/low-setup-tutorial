import bspump
import bspump.trigger
import bspump.common
import bspump.kafka

from .source.random_number_source import RandomNumberSource

class BitSwanTutorialPump(bspump.Pipeline):
    def __init__(self, app, pipeline_id):
        super().__init__(app, pipeline_id)


        self.build(
            RandomNumberSource(app, self).on(bspump.trigger.PeriodicTrigger(app, 1)),

            bspump.common.PPrintProcessor(app, self),

            bspump.common.StdDictToJsonParser(app, self),

            bspump.common.StringToBytesParser(app, self),


            # At the end of the pump pipeline, we need to add a sink.
            # When you first open the file, you will see that the NullSink is used.
            # This means that he event will be dumped at the end of the cycle.
            # If you want to use Kafka, you can uncomment the KafkaSink and comment the NullSink.

            bspump.common.NullSink(app, self)

            # bspump.kafka.KafkaSink(app, self, "KafkaConnection")

            # Don't forget to uncomment kafka connection in app.py
            )
