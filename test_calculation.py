import pytest

import caluculation

is_release = True

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = caluculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def test_add_num_add_double(self):
        assert self.cal.add_num_and_double(1, 1, ) == 4

    @pytest.mark.skipif(is_release==True, reason='skip')
    def test_add_num_add_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')