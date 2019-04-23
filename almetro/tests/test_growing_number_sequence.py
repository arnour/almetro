"""
GrowingNumberSequenceProvider test.

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

from almetro.instance import GrowingNumberSequenceProvider


def test_should_return_new_sized_7_sequence():
    assert_that(GrowingNumberSequenceProvider(size=7).new(), has_length(7))


def test_should_return_new_randomic_sequence():
    instance = GrowingNumberSequenceProvider(size=3).new()
    assert_that(instance[0], is_not(equal_to(instance[1])))
    assert_that(instance[0], is_not(equal_to(instance[2])))

def test_should_return_grown_sequence():
    sequence = GrowingNumberSequenceProvider(size=10, growth_rate=0.5)
    assert_that(sequence.new(), has_length(10))
    assert_that(sequence.new(), has_length(15))
    assert_that(sequence.new(), has_length(20))
    assert_that(sequence.new(), has_length(25))

def test_should_return_static_grown_sequence():
    sequence = GrowingNumberSequenceProvider(size=0, growth_size=100)
    assert_that(sequence.new(), has_length(0))
    assert_that(sequence.new(), has_length(100))
    assert_that(sequence.new(), has_length(200))
    assert_that(sequence.new(), has_length(300))    
