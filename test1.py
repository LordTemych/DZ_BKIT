import unittest
import sys, os

sys.path.append(os.getcwd())
from bot2 import *

test1 = 1
test2 = 2
test3 = 3

class TestGetRoots(unittest.TestCase):
    def test1_bot(self):
        res = summary(material,material_price,equip,equip_price,fasteners,fasteners_price,test1,test2,test3)
        self.assertEqual("Итого = 670\n", res)
    def test2_bot(self):
        res = summary(material,material_price,equip,equip_price,fasteners,fasteners_price,test2,test1,test3)
        self.assertEqual("Итого = 310\n", res)

if __name__ == "__main__":
    unittest.main()