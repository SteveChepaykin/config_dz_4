from main import assemble, interpret, UVMMemory 
import unittest
import os.path as p

class TestMethods(unittest.TestCase):
    def test_assembly(self):
        assemble("test.xml")
        self.assertTrue(p.isfile("binary.txt"))

    def test_interpretation(self):
        if(p.isfile("binary.txt")):
            interpret()
            self.assertTrue(p.isfile("out.txt"))

    def test_mem_create(self):
        print()

    def test_mem_load(self):
        print()
    
    def test_mem_read(self):
        print()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)