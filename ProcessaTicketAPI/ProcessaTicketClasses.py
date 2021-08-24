import datetime as dt
import json
from settings import VALID_OPERATIONS


class TicketProcessor(object):
    def __init__(self, request: json):
        self._request = request
        self._timestamp = dt.datetime.utcnow()

    def process(self):

        data = self._request

        # attempts to calculate operation related to given code
        proc_req = self.process_calculation_by_code(data['code'])

        # store process request
        self.store_request(proc_req)

        return proc_req

    def process_calculation_by_code(self, code):

        proc_req = {
            'succesful': 'no',
            'operation': None,
            'val': None,
            'code': code,
            'timestamp': self._timestamp
        }

        with open('../Infrastructure/tickreq_db.txt', 'r') as f:

            try:
                for req in calculation_requests := f.read().split('#'):
                    if bool(req['is_valid']) and req['code'] == code:

                        v1, v2, op = req['val1'], req['val2'], req['operation']

                        proc_req['val'] = self.operate(v1, v2, op)

                        proc_req['operation'] = f'{v1} {op} {v2}'

                        proc_req['succesful'] = 'yes'

                        break

            except Exception as e:

                proc_req['sucessful'] = 'no'

                proc_req['error'] = e

            finally:
                f.close()

        return proc_req

    @staticmethod
    def store_request(request):
        with open('../Infrastructure/tickprocs_db.txt', 'a') as f:
            try:
                f.write(
                    json.dumps(request, indent=4, default=str) + '\n#\n'
                )

            except TypeError as e:
                print(f'{e}')
                f.write(
                    json.dumps(request, indent=4, default=str, skip=True) + '\n#\n'
                )

            finally:
                f.close()

    @staticmethod
    def operate(v1, v2, op):
        return VALID_OPERATIONS[op](v1, v2)
