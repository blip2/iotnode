from iotnode.controller import Controller
from config import MODULES

node = Controller(MODULES)
node.start()
