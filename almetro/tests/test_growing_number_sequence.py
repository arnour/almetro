"""
GrowingNumberSequenceProvider test.

"""
from almetro.tests import TestBase, matchers as m
from almetro.instance import GrowingNumberSequenceProvider


class TestChart(TestBase):

    def test_should_return_new_sized_7_sequence(self):
        m.assert_that(GrowingNumberSequenceProvider(initial_size=7).new_instance(), m.has_length(7))

    def test_should_return_new_randomic_sequence(self):
        instance = GrowingNumberSequenceProvider(initial_size=3).new_instance()
        m.assert_that(instance[0], m.is_not(m.equal_to(instance[1])))
        m.assert_that(instance[0], m.is_not(m.equal_to(instance[2])))

    def test_should_return_grown_sequence(self):
        sequence = GrowingNumberSequenceProvider(initial_size=10, growth_rate=0.5)
        m.assert_that(sequence.new_instance(), m.has_length(10))
        m.assert_that(sequence.new_instance(), m.has_length(15))
        m.assert_that(sequence.new_instance(), m.has_length(20))
        m.assert_that(sequence.new_instance(), m.has_length(25))

    def test_should_return_static_grown_sequence(self):
        sequence = GrowingNumberSequenceProvider(initial_size=0, growth_size=100)
        m.assert_that(sequence.new_instance(), m.has_length(0))
        m.assert_that(sequence.new_instance(), m.has_length(100))
        m.assert_that(sequence.new_instance(), m.has_length(200))
        m.assert_that(sequence.new_instance(), m.has_length(300))
