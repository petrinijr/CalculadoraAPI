import datetime as dt
import json


class TicketGenerator:
    def __init__(self):
        self._timestamp = dt.datetime.now()

    @classmethod
    def calculate(cls, request: json):
        return request
