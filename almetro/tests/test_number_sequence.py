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


def test_should_return_new_sized_7_sequence():
    assert_that(NumberSequence(size=7).new(), has_length(7))


def test_should_return_new_randomic_sequence():
    instance = NumberSequence(size=3).new()
    assert_that(instance[0], is_not(equal_to(instance[1])))
    assert_that(instance[0], is_not(equal_to(instance[2])))


def test_should_return_new_rounded_2_digits_sequence():
    assert_that(tuple(map(str, NumberSequence(size=3, digits=2).new())), has_items(matches_regexp("^[0-9]\\.[0-9]{2}$")))


def test_should_return_grown_sequence():
    sequence = NumberSequence(size=10, growth_rate=0.5)
    assert_that(sequence.new(), has_length(10))
    assert_that(sequence.new(), has_length(15))
    assert_that(sequence.new(), has_length(20))
    assert_that(sequence.new(), has_length(25))
