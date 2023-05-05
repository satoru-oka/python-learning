import pytest

import caluculation

# def test_add_num_and_double():
    # cal = caluculation.Cal()
    # assert cal.add_num_and_double(1, 1, ) != 4
    # assert cal.add_num_and_double(1, 1, ) == 4

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = caluculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = caluculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal
    def test_add_num_add_double(self):
        assert self.cal.add_num_and_double(1, 1, ) == 4

    def test_add_num_add_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')