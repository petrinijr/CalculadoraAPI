import datetime as dt
import json


class TicketGenerator(object):
    def __init__(self):
        self._timestamp = dt.datetime.now()

    @classmethod
    def process(cls, request: json):
        return request
