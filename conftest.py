import os
import pytest

@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before')
        yield c
        print('after')

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')