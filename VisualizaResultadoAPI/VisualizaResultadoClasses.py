import datetime as dt
import json
import os
from settings import VALID_OPERATIONS, ROOT_DIR


class TicketRetriever(object):
    def __init__(self, request: json):
        self._request = request
        self._timestamp = dt.datetime.utcnow()

    def process(self):

        data = self._request

        # attempts to retrieve calculation related to given code
        if isinstance(
            value := self.retrieve_calculation_by_code(data['code']),
            float
        ):
            return {
                'timestamp': self._timestamp,
                'code': data['code'],
                'val': value,
                'request': self._request,
                'successful': 'true'
            }

        else:

            return {
                'timestamp': self._timestamp,
                'code': data['code'],
                'val': None,
                'request': self._request,
                'successful': 'false'
            }

    def retrieve_calculation_by_code(self, code):

        data = self._request

        with open(
            file=os.path.join(ROOT_DIR, 'Infrastructure', 'tickprocs_db.txt'),
            mode='r'
        ) as f:

            for req_str in (
                    calculation_requests := f.read().split('#')
            ):
                try:
                    process_req = json.loads(req_str)

                    if isinstance(process_req['val'], float) and process_req['code']:
                        if process_req['code'] == code:

                            return process_req['val']

                except json.JSONDecodeError:
                    pass
