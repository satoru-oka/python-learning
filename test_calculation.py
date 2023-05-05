import caluculation

# def test_add_num_and_double():
    # cal = caluculation.Cal()
    # assert cal.add_num_and_double(1, 1, ) != 4
    # assert cal.add_num_and_double(1, 1, ) == 4

class TestCal(object):
    def test_add_num_add_double(self):
        cal = caluculation.Cal()
        assert cal.add_num_and_double(1, 1, ) == 4