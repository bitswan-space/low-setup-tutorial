import bspump
import bspump.kafka

from .pipeline import BitSwanTutorialPump

class BitSwanTutorialApp(bspump.BSPumpApplication):
    def __init__(self):
        super().__init__()

        svc = self.get_service("bspump.PumpService")

        # svc.add_connection(bspump.kafka.KafkaConnection(self, "KafkaConnection"))

        svc.add_pipeline(BitSwanTutorialPump(self, "BitSwanTutorialPump"))
