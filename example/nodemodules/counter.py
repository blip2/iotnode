from iotnode.module import NodeModule
import time


class CounterModule(NodeModule):
    i = 0

    def tick(self):
        self.store("counter", self.i)
        self.i += 1
        self.push({
            "type": "influx",
            "data": "blah"
        })
        time.sleep(1)
