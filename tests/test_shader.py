import unittest

import simsteg.shader as shader


class ClampCase(unittest.TestCase):
    
    """Test clamping of values to valid range."""
    
    def test_clamp8(self):
        clamp8 = shader.clamp8
        self.assertEqual(clamp8(1000), 255)
        self.assertEqual(clamp8(-10), 0)
        self.assertEqual(clamp8(20.7), 21)
    
    def test_clamp_pixel(self):
        self.assertEqual(shader.clamp_pixel((1000, -10, 20.7)),
                         (255, 0, 21))

class ShaderCase(unittest.TestCase):
    
    """Test creation and application of shaders."""
    
    def setUp(self):
        self.data = [[(1, 2, 3), (4, 5, 6)],
                     [(7, 8, 9), (10, 11, 12)]]
        self.data2 = [[(1, 4, 9), (16, 25, 36)],
                      [(49, 64, 81), (100, 121, 144)]]
        self.data3 = [[(2, 6, 12), (20, 30, 42)],
                      [(56, 72, 90), (110, 132, 156)]]
    
    def test_shader(self):
        def f(i):
            return i**2
        sh = shader.make_shader(f)
        shader.apply_shader(self.data, sh)
        self.assertEqual(self.data, self.data2)
    
    def test_shader2(self):
        def f(i, j):
            return i + j
        sh = shader.make_shader2(f)
        shader.apply_shader2(self.data, self.data2, sh)
        self.assertEqual(self.data, self.data3)


if __name__ == '__main__':
    unittest.main()
