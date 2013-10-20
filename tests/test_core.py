import unittest

from simsteg.core import dataify, stringify, load_image_data, save_image_data


class FormatCase(unittest.TestCase):
    
    """Test conversion to/from internal format."""
    
    def setUp(self):
        self.buf = list([i * 10 + j * 3 + k
                         for i in range(4)
                         for j in range(3)
                         for k in range(3)])
        self.buf = ''.join(chr(i) for i in self.buf)
        self.data = [[tuple(i * 10 + j * 3 + k for k in range(3))
                      for j in range(3)]
                     for i in range(4)]
    
    def test_dataify(self):
        data = dataify(self.buf, 3, 4)
        self.assertEqual(data, self.data)
    
    def test_stringify(self):
        buf = stringify(self.data)
        self.assertEqual(buf, self.buf)


if __name__ == '__main__':
    unittest.main()
