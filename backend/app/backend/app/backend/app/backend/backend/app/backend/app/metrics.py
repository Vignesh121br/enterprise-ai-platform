import time


class Metrics:

    def latency(self, start):

        return round(
            time.time() - start,
            4
        )


metrics = Metrics()
