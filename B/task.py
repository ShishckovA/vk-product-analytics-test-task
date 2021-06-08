import sys
import time
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class Task:
    def __init__(self, value, id_):
        self.status = 'ready'
        self.value = value
        self.id = id_

    def execute(self):
        logging.info(f"Started task {self.id}")

        new_value = self.value ** 2
        time.sleep(10 - self.id)
        self.value = new_value
        self.status = "completed"

        logging.info(f"Task {self.id} completed")
        return self.value
