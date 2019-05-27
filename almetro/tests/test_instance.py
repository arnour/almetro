"""
InstanceProvider test.

"""
from almetro.tests import TestBase, matchers as m
from almetro.instance import ValuesProvider, GeneratorProvider, GrowingNumberSequenceProvider
from almetro.instance import growing, generator, values, Instance
from almetro.complexity import cn_quadratic, cn_cubic


class TestInstance(TestBase):

    def test_should_return_values_provider(self):
        provider = values([
            {'name': 'values', 'size': {'n': 3}, 'value': {'instance': [1, 2, 6]}},
            {'name': 'values', 'size': {'n': 6}, 'value': {'instance': [1, 2, 6, 10, 20, 60]}}
        ])
        m.assert_that(provider, m.instance_of(ValuesProvider))

        instance = provider.new_instance()
        m.assert_that(instance.name, m.equal_to('values'))
        m.assert_that(instance.label, m.equal_to('values n=3'))
        m.assert_that(instance.size['n'], m.equal_to(3))
        m.assert_that(instance.value['instance'], m.equal_to([1, 2, 6]))

        instance = provider.new_instance()
        m.assert_that(instance.name, m.equal_to('values'))
        m.assert_that(instance.label, m.equal_to('values n=6'))
        m.assert_that(instance.size['n'], m.equal_to(6))
        m.assert_that(instance.value['instance'], m.equal_to([1, 2, 6, 10, 20, 60]))

    def test_should_return_growing_provider(self):
        provider = growing(initial_size=1, growth_rate=1.0)
        m.assert_that(provider, m.instance_of(GrowingNumberSequenceProvider))

        instance = provider.new_instance()
        m.assert_that(instance.name, m.equal_to('growing'))
        m.assert_that(instance.label, m.equal_to('growing n=1'))
        m.assert_that(instance.size['n'], m.equal_to(1))
        m.assert_that(instance.value['instance'], m.has_length(1))

        instance = provider.new_instance()
        m.assert_that(instance.name, m.equal_to('growing'))
        m.assert_that(instance.label, m.equal_to('growing n=2'))
        m.assert_that(instance.size['n'], m.equal_to(2))
        m.assert_that(instance.value['instance'], m.has_length(2))

        instance = provider.new_instance()
        m.assert_that(instance.name, m.equal_to('growing'))
        m.assert_that(instance.label, m.equal_to('growing n=3'))
        m.assert_that(instance.size['n'], m.equal_to(3))
        m.assert_that(instance.value['instance'], m.has_length(3))

    def test_should_return_generator_provider(self):
        def my_gen():
            for i in range(1, 3):
                yield {'name': 'range', 'size': {'n': i}, 'value': {'instance': range(i)}}

        provider = generator(my_gen())
        m.assert_that(provider, m.instance_of(GeneratorProvider))

        instance = provider.new_instance()

        m.assert_that(instance.name, m.equal_to('range'))
        m.assert_that(instance.label, m.equal_to('range n=1'))
        m.assert_that(instance.size['n'], m.equal_to(1))
        m.assert_that(instance.value['instance'], m.has_length(1))

        instance = provider.new_instance()

        m.assert_that(instance.name, m.equal_to('range'))
        m.assert_that(instance.label, m.equal_to('range n=2'))
        m.assert_that(instance.size['n'], m.equal_to(2))
        m.assert_that(instance.value['instance'], m.has_length(2))

    def test_should_return_theoretical_complexity(self):
        instance = Instance(name='instance', size={'n': 10}, value={'instance': range(10)})
        m.assert_that(instance.theoretical(cn_quadratic), m.equal_to(100))
        m.assert_that(instance.theoretical(cn_cubic), m.equal_to(1000))
