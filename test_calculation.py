import os
import pytest
import caluculation

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = caluculation.Cal()
        cls.test_file_name = 'text.txt'

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def test_add_num_add_double(self, tmpdir):
        print(tmpdir)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True