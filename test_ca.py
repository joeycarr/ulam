
import unittest

from ca import *
import random

class TestCA(unittest.TestCase):
    
    def test_unpack(self):
        self.assertEqual( unpack(10, 8), [2,1] )
        self.assertEqual( unpack(10, 7), [3,1] )
        self.assertEqual( unpack(10, 6), [4,1] )
        self.assertEqual( unpack(10, 5), [0,2] )
        self.assertEqual( unpack(10, 4), [2,2] )
        self.assertEqual( unpack(10, 3), [1,0,1] )
        self.assertEqual( unpack(10, 2), [0,1,0,1] )
        self.assertEqual( unpack(11, 2), [1,1,0,1] )
        self.assertEqual( unpack(12, 2), [0,0,1,1] )
        self.assertEqual( unpack(13, 2), [1,0,1,1] )
        self.assertEqual( unpack(14, 2), [0,1,1,1] )

    def test_pack(self):
        self.assertEqual( [2,1],     unpack(10, 8) )
        self.assertEqual( [3,1],     unpack(10, 7) )
        self.assertEqual( [4,1],     unpack(10, 6) )
        self.assertEqual( [0,2],     unpack(10, 5) )
        self.assertEqual( [2,2],     unpack(10, 4) )
        self.assertEqual( [1,0,1],   unpack(10, 3) )
        self.assertEqual( [0,1,0,1], unpack(10, 2) )
        self.assertEqual( [1,1,0,1], unpack(11, 2) )
        self.assertEqual( [0,0,1,1], unpack(12, 2) )
        self.assertEqual( [1,0,1,1], unpack(13, 2) )
        self.assertEqual( [0,1,1,1], unpack(14, 2) )
        
    def test_symetry(self):
        '''This test takes a long time (six seconds), but it tests the symetry of packing and unpacking through some very large values.'''
        for code in range( 2**12 ):
            for radix in range( 2, 2**8 ):
                self.assertEqual( code, pack( unpack(code, radix), radix ))

    def test_neighborhood(self):
        self.assertEqual(list('def'),
                         list(neighborhood(list('abcdefg'), 4, 1)))
        self.assertEqual(list('bcdef'),
                         list(neighborhood(list('abcdefg'), 3, 2)))
        self.assertEqual(list('fab'),
                         list(neighborhood(list('abcdef'), 0, 1)))
        self.assertEqual(list('cdefgab'),
                         list(neighborhood(list('abcdefg'), 5, 3)))

    def test_carule(self):
        rule = carule(90, 2, 1)
        self.assertEqual([0,0,0], rule([0,0,0]))
        self.assertEqual([1,1,0], rule([0,0,1]))
        self.assertEqual([1,0,1], rule([0,1,0]))
        self.assertEqual([0,1,1], rule([0,1,1]))
        self.assertEqual([0,1,1], rule([1,0,0]))
        self.assertEqual([1,0,1], rule([1,0,1]))
        self.assertEqual([1,1,0], rule([1,1,0]))
        self.assertEqual([0,0,0], rule([1,1,1]))

    def test_lookup(self):
        looker = lookup(90, 2, 1)
        self.assertEqual(0, looker(pack([1,1,1], 2)))
        self.assertEqual(1, looker(pack([1,1,0], 2)))
        self.assertEqual(0, looker(pack([1,0,1], 2)))
        self.assertEqual(1, looker(pack([1,0,0], 2)))
        self.assertEqual(1, looker(pack([0,1,1], 2)))
        self.assertEqual(0, looker(pack([0,1,0], 2)))
        self.assertEqual(1, looker(pack([0,0,1], 2)))
        self.assertEqual(0, looker(pack([0,0,0], 2)))

    def test_getrandcode(self):
        random.seed(1)
        code1 = getrandcode(8,1)
        random.seed(1)
        code2 = getrandcode(8,1)
        self.assertEqual( code1, code2 )
        random.seed(2)
        code1 = getrandcode(4,2)
        code2 = getrandcode(4,2)
        # There's a very, very small chance this could fail at random
        self.assertNotEqual(code1, code2)

if __name__ == '__main__':
    unittest.main()
