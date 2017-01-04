import unittest
from src_code import *
import sys


def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print '  %s src_file %s line %s' % (filename, func_name, line_no)


def my_debug(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name in TRACE_INFO:
        # Trace into this function
        return trace_lines
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    print 'Call to %s on line %s of %s from line %s of %s' % \
        (func_name, func_line_no, func_filename,
         caller_line_no, caller_filename)
    return

TRACE_INFO = ['increase_n']
sys.settrace(my_debug)


class TestStubClass(unittest.TestCase):

    ins_stub = None

    def setUp(self):
        self.ins_stub = StubClass()
        print "setup..."

    def tearDown(self):
        print "teardown..."

    def test_increase_n(self):
        self.assertTrue(self.ins_stub.increase_n() == 1)
        print "testing..."
