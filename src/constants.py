from pathlib import Path


MAIN_DOC_URL = 'https://docs.python.org/3/'

PEPS_URL = 'https://peps.python.org/'

BASE_DIR = Path(__file__).parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

DT_FORMAT = '%d.%m.%Y %H:%M:%S'

EXPECTED_STATUS = {
    'Active': 0,
    'Accepted': 0,
    'Deferred': 0,
    'Final': 0,
    'Rejected': 0,
    'Superseded': 0,
    'Withdrawn': 0,
    'Draft': 0
}
