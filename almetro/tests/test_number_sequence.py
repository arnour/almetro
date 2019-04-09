"""
NumberSequence test.

"""
from hamcrest import (
    assert_that,
    instance_of,
    has_length,
    has_items,
    matches_regexp,
    is_not,
    equal_to,
)

from almetro.instance import NumberSequence


def test_should_return_immutable_sequence():
    sequence = NumberSequence()
    assert_that(sequence.get(), instance_of(tuple))


def test_should_return_a_size_3_sequence():
    sequence = NumberSequence(size=3)
    assert_that(sequence.get(), has_length(3))


def test_should_return_a_randomic_sequence():
    sequence = NumberSequence(size=3)
    assert_that(sequence.get()[0], is_not(equal_to(sequence.get()[1])))
    assert_that(sequence.get()[0], is_not(equal_to(sequence.get()[2])))


def test_should_return_rounded_2_digits_sequence():
    sequence = NumberSequence(size=3, digits=2)
    assert_that(tuple(map(str, sequence.get())), has_items(matches_regexp("^[0-9]\\.[0-9]{2}$")))
