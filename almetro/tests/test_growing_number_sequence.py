"""
GrowingNumberSequenceProvider test.

"""
from almetro.tests import TestBase, matchers as m
from almetro.instance import GrowingNumberSequenceProvider


class TestGrowingNumberSequenceProvider(TestBase):

    def test_should_return_new_sized_7_sequence(self):
        instance = GrowingNumberSequenceProvider(initial_size=7).new_instance()
        m.assert_that(instance.value['instance'], m.has_length(7))
        m.assert_that(instance.size['n'], m.equal_to(7))
        m.assert_that(instance.name, m.equal_to('growing'))

    def test_should_return_new_randomic_sequence(self):
        instance = GrowingNumberSequenceProvider(initial_size=3).new_instance().value['instance']
        m.assert_that(instance[0], m.is_not(m.equal_to(instance[1])))
        m.assert_that(instance[0], m.is_not(m.equal_to(instance[2])))

    def test_should_return_grown_sequence(self):
        provider = GrowingNumberSequenceProvider(initial_size=10, growth_rate=0.5)

        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(10))
        m.assert_that(instance.value['instance'], m.has_length(10))
        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(15))
        m.assert_that(instance.value['instance'], m.has_length(15))
        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(20))
        m.assert_that(instance.value['instance'], m.has_length(20))
        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(25))
        m.assert_that(instance.value['instance'], m.has_length(25))

    def test_should_return_grown_sequence_starting_empty(self):
        provider = GrowingNumberSequenceProvider(initial_size=0, growth_size=100)

        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(0))
        m.assert_that(instance.value['instance'], m.has_length(0))

        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(100))
        m.assert_that(instance.value['instance'], m.has_length(100))

        instance = provider.new_instance()
        m.assert_that(instance.size['n'], m.equal_to(200))
        m.assert_that(instance.value['instance'], m.has_length(200))
