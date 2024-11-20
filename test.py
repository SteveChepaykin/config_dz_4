from main import assemble, process_command, execute_instructions
import unittest
import os.path as p

class TestMethods(unittest.TestCase):
    def test_commands(self):
        const = process_command(0, 7, 555, 3)
        get = process_command(14, 6, 1, 2)
        put = process_command(10, 2, 424, 4)
        neg = process_command(4, 0, 61, 4)
        self.assertEqual(const, b'\xf0\x15\x01')
        self.assertEqual(get, b'\xee\x00')
        self.assertEqual(put, b'\x2a\xd4\x00\x00')
        self.assertEqual(neg, b'\x84\x1e\x00\x00')

    def test_assembly(self):
        assemble("test.txt")
        self.assertTrue(p.isfile("binary.txt"))

    def test_interpretation(self):
        if(p.isfile("binary.txt")):
            execute_instructions()
            self.assertTrue(p.isfile("log.xml"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)