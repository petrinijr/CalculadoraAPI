import datetime as dt
import json
import os
from settings import VALID_OPERATIONS, ROOT_DIR


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
            'successful': 'fase',
            'operation': None,
            'val': None,
            'code': code,
            'timestamp': self._timestamp
        }

        with open(
            file=os.path.join(ROOT_DIR, 'Infrastructure', 'tickreq_db.txt'),
            mode='r'
        ) as f:

            for req_str in (
                    calculation_requests := f.read().split('#')
            ):

                try:

                    enh_req = json.loads(req_str)

                    if enh_req['is_valid'] and enh_req['code'] == code:

                        req = enh_req['request']

                        v1, v2, op = req['val1'], req['val2'], req['operation']

                        proc_req['val'] = self.operate(v1, v2, op)

                        proc_req['operation'] = f'{v1} {op} {v2}'

                        proc_req['successful'] = 'true'

                        break

                except json.JSONDecodeError:

                    proc_req['successful'] = 'false'

                    proc_req['error'] = 'Not found.'

                except Exception as e:

                    proc_req['successful'] = 'false'

                    proc_req['error'] = e.__str__()

        return proc_req

    @staticmethod
    def store_request(request):

        with open(
                file=os.path.join(ROOT_DIR, 'Infrastructure', 'tickprocs_db.txt'),
                mode='a'
        ) as f:

            try:
                f.write(
                    json.dumps(request, indent=4, default=str) + '\n#\n'
                )

            except TypeError as e:
                f.write(
                    json.dumps(request, indent=4, default=str, skip=True) + '\n#\n'
                )

            finally:
                f.close()

    @staticmethod
    def operate(v1, v2, op):
        return VALID_OPERATIONS[op](float(v1), float(v2))
