from math import sqrt

import random

MIN_LEN = 10 ** 6
MAX_LEN = 10 ** 7


class Stream:
    def __init__(self, host, port):
        """
        Stream: simulates measurement stream from the sensor
        """
        self.host = host
        self.port = port
        self.len = random.randint(MIN_LEN, MAX_LEN)
        self.pos = 0

    def has_next(self):
        """
        Checks if there is next value in stream
        return: bool
        """
        return self.pos < self.len

    def next_value(self):
        """
        Returns next received value
        return: float
        """
        if self.pos >= self.len:
            raise IndexError("Stream is closed")

        self.pos += 1

        return random.random() * 2 - 1


def calc_std(s, sq_s, n):
    if n <= 1:
        return 0
    return sqrt((sq_s - (s * s) / n) / n)


host = "localhost"
port = 82
stream = Stream(port=port, host=host)

v_sum = 0
v_sq_sum = 0
v_n = 0

while stream.has_next():
    value = stream.next_value()

    v_n += 1
    v_sum += value
    v_sq_sum += value * value

    std_value = calc_std(v_sum, v_sq_sum, v_n)

    print(std_value)
