"""
NumberSequence test.

"""
from hamcrest import (
    assert_that,
    instance_of,
)

from almetro.instance import NumberSequence


def test_should_return_immutable_sequence():
    sequence = NumberSequence()
    assert_that(sequence.values(), instance_of(tuple))
