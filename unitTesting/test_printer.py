from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    def setUp(self):
        print("init test")
        self.printer = Printer(300)

    def test_print_within_capacity(self):
        print("tc-1")
        message = self.printer.print(25)
        self.assertEqual("printed 25 pages.", message)

    def test_print_outside_capacity(self):
        print("tc-2")
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        print("tc-3")
        self.printer.print(self.printer.capacity)

    def test_remaining_pages(self):
        print("tc-4")
        self.printer.print(50)
        self.assertEqual(250, self.printer.remaining_pages)

