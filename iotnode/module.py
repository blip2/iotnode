import time
import logging


class NodeModule(object):
    active = False

    def __init__(self, mbus, queue, active, stop, cache):
        """Create the module, receives the message bus and queue"""
        self.id = self.__class__.__name__
        self.__mbus = mbus
        self.queue = queue
        self.__active = active
        self.__stop = stop
        self.__changed = True
        self.cache = cache

    def worker(self):
        while True:
            if self.__stop.is_set():
                self.cleanup()
                break
            if self.__active.is_set() and not self.active:
                self.active = True
                self.__changed = True
            elif self.active and not self.__active.is_set():
                self.active = False
            try:
                if not self.queue.empty():
                    self.processQueue(self.queue.get())
                else:
                    self.tick()
            except Exception as e:
                logging.exception("Exception in worker")
                time.sleep(5)

    def cleanup(self):
        pass

    def processQueue(self, data):

        callback = getattr(self, "callback_" + data["type"], None)

        if data["type"] == "shutdown":
            exit()

        elif data["type"] == "__icache":
            self.cache = data["data"]

        elif callable(callback):
            callback(data)

        else:
            self.processMessage(data)

    def add_to_menu(self, title):
        self.push({'type': 'menu_add', 'title': title})

    def update(self):
        self.__changed = True

    def store(self, key, value):
        data = {"type": "store", "key": key, "value": value}
        self.__mbus.put(data)

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

    def push(self, data):
        if "type" not in data:
            data = {"type": "unspecified", "data": data, }
        data['_source'] = self.id
        self.__mbus.put(data)

    def pushToModule(self, name, data):
        data["target"] = name
        self.__send(data)

    def wait(self, wait=None):
        if self.active and self.__changed:
            if callable(getattr(self, "draw", None)):
                self.__changed = False
                self.draw()
        if wait:
            time.sleep(wait)
        elif self.active:
            time.sleep(0.2)
        else:
            self.processQueue(self.queue.get(True))

    def tick(self):
        self.wait()

    def processMessage(self, data):
        pass
