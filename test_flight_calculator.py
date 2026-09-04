import pytest
from flight_calculator import calculate_flight_time
def test_zero_weight():
    assert calculate_flight_time(0) == 180


def test_typical_weight():
        assert calculate_flight_time(100) == 170

def test_boundary_to_zero():
            assert calculate_flight_time(1800) == 0

def test_negative_weight():
                with pytest.raises(ValueError):
                    calculate_flight_time(-50)