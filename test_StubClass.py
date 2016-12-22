import nose
import nose.plugins.cover
import unittest
import coverage
from src_code import *


class TestStubClass(unittest.TestCase):

    ins_stub = None

    def setUp(self):
        self.ins_stub = StubClass()

    def tearDown(self):
        pass

    def test_increase_n(self):
        self.assertTrue(self.ins_stub.increase_n() == 1)
