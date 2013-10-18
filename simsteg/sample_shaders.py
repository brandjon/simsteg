# sample_shaders.py: Example pixel and intensity shaders.


from shader import make_shader 


# Intensity shaders.

def int_brighten(v, offset):
    return v + offset

def int_contrast(v, factor):
    b = 128 * (1 - factor)
    return (float(v) * factor) + b

def int_gamma(v, g):
    return ((float(v)/256) ** (1./g)) * 256

def int_flatten(v, k):
    """Truncate the k lowest bits to 0."""
    return v & ~(2**k - 1)

def int_addnoise(v, k):
    """Randomize the k lowest bits."""
    if k == 0:
        return v
    
    from random import getrandbits
    mask = ~(2**k - 1)
    return (v & mask) | getrandbits(k)

def int_invert(v, k):
    return 255 - v


# Pixel shaders.

brighten = make_shader(int_brighten)
contrast = make_shader(int_contrast)
gamma = make_shader(int_gamma)
flatten = make_shader(int_flatten)
addnoise = make_shader(int_addnoise)
invert = make_shader(int_invert)

def random_grey(pixel):
    from random import randint
    v = randint(0, 255)
    return (v, v, v)

def random_color(pixel):
    from random import randint
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def swap_colors(pixel):
    red, green, blue = pixel
    return green, blue, red
