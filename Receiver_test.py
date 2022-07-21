from Receiver import *
import mock


def test_update_max_value():
    signal_stats = SignalStatistic()
    signal_stats.update_max_value(100, 10)
    assert(signal_stats.max_temp_value == 100)
    assert(signal_stats.max_charge_value == 10)

    signal_stats.update_max_value(101, 11)
    assert(signal_stats.max_temp_value == 101)
    assert(signal_stats.max_charge_value == 11)

    signal_stats.update_max_value(99, 9)
    assert(signal_stats.max_temp_value == 101)
    assert(signal_stats.max_charge_value == 11)


def test_update_min_value():
    signal_stats = SignalStatistic()
    signal_stats.update_min_value(100, 10)
    assert(signal_stats.min_temp_value == 100)
    assert(signal_stats.min_charge_value == 10)

    signal_stats.update_min_value(99, 9)
    assert (signal_stats.min_temp_value == 99)
    assert (signal_stats.min_charge_value == 9)

    signal_stats.update_min_value(101, 11)
    assert(signal_stats.min_temp_value == 99)
    assert(signal_stats.min_charge_value == 9)


def test_update_moving_avg():
    signal_stats = SignalStatistic()
    signal_stats.update_moving_avg(100, 10)
    assert(signal_stats.temp_avg == 100)
    assert(signal_stats.charge_avg == 10)

    # add 4 more signal values to calc avg of 5
    signal_stats.update_moving_avg(101, 11)
    signal_stats.update_moving_avg(102, 12)
    signal_stats.update_moving_avg(103, 13)
    signal_stats.update_moving_avg(104, 14)
    assert(signal_stats.temp_avg == 102)
    assert(signal_stats.charge_avg == 12)

    # test when more than 5 signals have been received
    signal_stats.update_moving_avg(105, 15)
    signal_stats.update_moving_avg(106, 16)
    assert(signal_stats.temp_avg == 104)
    assert(signal_stats.charge_avg == 14)


def test_derive_signal_values():
    temp, charge = derive_signal_values('{"Temperature": 42.8, "Charge Rate": 23}')
    assert(temp == 42.8)
    assert(charge == 23)

    temp, charge = derive_signal_values('{"Temperature": 130, "Charge Rate": 60}')
    assert(temp == 130)
    assert(charge == 60)


def test_process_input_signal():
    signal_stats = SignalStatistic()
    signal_stats.update_moving_avg = mock.Mock()
    signal_stats.update_min_value = mock.Mock()
    signal_stats.update_moving_avg = mock.Mock()
    process_input_signal('{"Temperature": 42.8, "Charge Rate": 23}', signal_stats)
    assert(signal_stats.update_moving_avg.call_count == 1)
    assert(signal_stats.update_min_value.call_count == 1)
    assert(signal_stats.update_moving_avg.call_count == 1)


def test_integration_process_input_signal():
    signal_stats = SignalStatistic()
    process_input_signal('{"Temperature": 42.8, "Charge Rate": 23}', signal_stats)
    assert(signal_stats.temp_avg == 42.8)
    assert(signal_stats.charge_avg == 23)
    assert(signal_stats.min_temp_value == 42.8)
    assert(signal_stats.max_temp_value == 42.8)
    assert(signal_stats.min_charge_value == 23)
    assert(signal_stats.max_charge_value == 23)

    process_input_signal('{"Temperature": 130.6, "Charge Rate": 60}', signal_stats)
    process_input_signal('{"Temperature": 110.0, "Charge Rate": 41}', signal_stats)
    process_input_signal('{"Temperature": 10.7, "Charge Rate": 11}', signal_stats)
    process_input_signal('{"Temperature": 67.4, "Charge Rate": 55}', signal_stats)
    process_input_signal('{"Temperature": 61.6, "Charge Rate": 32}', signal_stats)
    assert(signal_stats.temp_avg == 76.06)
    assert(signal_stats.charge_avg == 39.8)
    assert(signal_stats.min_temp_value == 10.7)
    assert(signal_stats.max_temp_value == 130.6)
    assert(signal_stats.min_charge_value == 11)
    assert(signal_stats.max_charge_value == 60)


if __name__ == '__main__':
    test_update_max_value()
    test_update_min_value()
    test_update_moving_avg()
    test_process_input_signal()
    test_integration_process_input_signal()
