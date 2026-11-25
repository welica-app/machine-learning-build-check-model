import pytest

from train import validate_inputs


def test_accepts_before_departure_input():
    validate_inputs(["queue_length"])


def test_rejects_unknown_input():
    with pytest.raises(ValueError):
        validate_inputs(["unknown_column"])


def test_rejects_after_departure_input():
    pytest.skip("TODO")
