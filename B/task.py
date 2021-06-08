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

        time.sleep(2)  # let's imagine task runs 2 seconds
        new_value = self.value ** 2
        self.value = new_value
        self.status = "completed"

        logging.info(f"Task {self.id} completed")
        return self.value
