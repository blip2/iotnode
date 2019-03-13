from iotnode.module import NodeModule
import logging


class TestModule(NodeModule):
    def callback_influx(self, data):
        logging.debug(data)
