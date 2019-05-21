from unittest import TestCase, SkipTest, mock
import hamcrest


class TestBase(TestCase):

    @classmethod
    def setUpClass(cls):
        if cls.__name__ == 'TestBase':
            raise SkipTest("Base class")
        super().setUpClass()


mock = mock
matchers = hamcrest
