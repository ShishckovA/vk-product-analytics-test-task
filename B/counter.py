import time


class Counter:
    def __init__(self):
        self.value = 0

    def update(self, new_value):
        local = self.value
        local += new_value
        time.sleep(0.1)
        self.value = local
