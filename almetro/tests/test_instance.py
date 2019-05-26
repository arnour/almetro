"""
InstanceProvider test.

"""
import random
from almetro.tests import TestBase, matchers as m
from almetro.instance import InstanceProvider, GeneratorProvider, GrowingNumberSequenceProvider
from almetro.instance import growing, generator


class TestInstance(TestBase):

    def test_should_return_randomic_arrays(self):
        provider = InstanceProvider(fn=lambda: random.sample(range(5), 5))

        m.assert_that(provider.new_instance(), m.has_length(5))
        m.assert_that(provider.new_instance(), m.has_length(5))

    def test_should_return_same_instance(self):
        provider = InstanceProvider(fn=lambda: [1, 2, 6])

        m.assert_that(provider.new_instance(), m.has_items(1, 2, 6))
        m.assert_that(provider.new_instance(), m.has_items(1, 2, 6))

    def test_should_return_growing_provider(self):
        provider = growing(initial_size=1, growth_rate=1.0)
        m.assert_that(provider, m.instance_of(GrowingNumberSequenceProvider))
        m.assert_that(provider.new_instance()['instance'], m.has_length(1))
        m.assert_that(provider.new_instance()['instance'], m.has_length(2))
        m.assert_that(provider.new_instance()['instance'], m.has_length(3))

    def test_should_return_generator_provider(self):
        def my_gen():
            yield {'instance': range(4)}
        provider = generator(my_gen)
        m.assert_that(provider, m.instance_of(GeneratorProvider))
        m.assert_that(provider.new_instance(), m.has_entry('instance', m.equal_to(range(4))))
