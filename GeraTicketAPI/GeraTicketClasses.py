import datetime as dt
import json
import alphabetic_timestamp as ats
from settings import VALID_OPERATIONS, VALID_RANGE


class TicketGenerator(object):
    def __init__(self, request: json):
        self._request = request
        self._timestamp = dt.datetime.utcnow()

    def process(self):
        is_valid, comment = self.check_request()

        enh_request = {
            'request': self._request,
            'timestamp': self._timestamp.isoformat(),
            'is_valid': is_valid,
            'comment': comment,
            'code': ats.base62.from_datetime(
                date_time=self._timestamp,
                time_unit=ats.TimeUnit.milliseconds,
            )
        }

        # store request
        self.store_request(enh_request)

        return enh_request

    def check_request(self) -> tuple:
        if not self._request:
            return False, 'No request.'

        data = self._request

        # Safeguarding against '#' character
        for field in data:
            if "#" in data[field]:
                data[field] = str(data[field]).replace("#", "<HASH>")

        # Operation validation
        try:
            if data['operation'] not in VALID_OPERATIONS:
                return False, 'Invalid operation.'
        except KeyError:
            return False, 'No operation.'

        # Value validation
        try:
            val1 = int(data['val1'])
            val2 = int(data['val2'])

            # avoid division by zero
            if val2 == 0 and data['operation'] == 'divided':
                return False, 'Division by zero'

            # avoid outside range
            if val1 < VALID_RANGE[0] or val1 >= VALID_RANGE[-1]:
                return False, 'Value 1 not in valid range.'
            if val2 < VALID_RANGE[0] or val2 >= VALID_RANGE[-1]:
                return False, 'Value 2 not in valid range.'

        except KeyError:
            return False, 'Missing values.'
        except TypeError:
            return False, 'Invalid value type passed.'

        return True, 'OK.'

    @staticmethod
    def store_request(request):
        with open('../Infrastructure/tickreq_db.txt') as f:
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
