import unittest

import simsteg.sample_shaders as samples


class SampleIntShaderCase(unittest.TestCase):
    
    """Test sample intensity shaders."""
    
    def test_brighten(self):
        self.assertEqual(samples.int_brighten(100, 5), 105)
    
    def test_contrast(self):
        self.assertEqual(samples.int_contrast(96, 2), 64)
        self.assertEqual(samples.int_contrast(128, 3), 128)
        self.assertEqual(samples.int_contrast(0, .5), 64)
    
    def test_gamma(self):
        self.assertEqual(samples.int_gamma(50, 1), 50)
        self.assertEqual(int(samples.int_gamma(50, 2)), 113)
        self.assertEqual(int(samples.int_gamma(50, .5)), 9)
    
    def test_flatten(self):
        self.assertEqual(samples.int_flatten(50, 3), 48)
        self.assertEqual(samples.int_flatten(45, 4), 32)
    
    # Hard to test addnoise as it's not deterministic.
    
    def test_invert(self):
        self.assertEqual(samples.int_invert(200), 55)


if __name__ == '__main__':
    unittest.main()
