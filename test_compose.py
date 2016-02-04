from unittest import TestCase
from compose import compose


class ComposeTests(TestCase):
    """
    Tests for L{compose.compose}.
    """
    def add_one(self, n):
        return n + 1

    def times_two(self, n):
        return n * 2

    def minus_three(self, n):
        return n - 3

    def test_one(self):
        """
        Composing one function is the same thing as just calling it.
        """
        self.assertEqual(
            2,
            compose(self.add_one)(1))
        self.assertEqual(
            self.add_one(1),
            compose(self.add_one)(1))

    def test_many(self):
        """
        Functions are applied from last to first.
        """
        self.assertEqual(
            -3,
            compose(self.add_one, self.times_two, self.minus_three)(1))

    def test_base_case(self):
        """
        [It is suggested](https://mathieularose.com/function-composition-in-python/#comment-1929127640)
        to define a base case for composition: The identity function.
        So `compose()` should be equal to the identity function *f(x) = x*.
        """
        f = compose() # This should not fail
        self.assertTrue(
            all(
                argument == f(argument) for argument in range(-1000, 1001)))
