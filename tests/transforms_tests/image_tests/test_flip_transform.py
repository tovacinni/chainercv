import unittest

import numpy as np

from chainer import testing
from chainercv.transforms import flip


class TestRandomFlipTransform(unittest.TestCase):

    def test_random_flip(self):
        x = np.random.uniform(size=(3, 24, 24))

        out = flip(x, horizontal=True, vertical=True)

        expected = x
        expected = expected[:, :, ::-1]
        expected = expected[:, ::-1, :]
        np.testing.assert_equal(out, expected)


testing.run_module(__name__, __file__)
