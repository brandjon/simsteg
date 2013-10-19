# shader.py: Image shader framework.


# I'm borrowing (abusing) the terminology "shader" from graphics
# hardware. I use "shader" to refer to a function that takes in a pixel
# and returns a pixel. I use "intensity shader" to refer to a function
# that takes in an 8-bit value and returns an 8-bit value.


def clamp8(v):
    """Given a value, cut it off so it's an integer within the range
    [0, 255].
    """
    if v < 0:
        return 0
    elif v > 255:
        return 255
    else:
        return int(round(v))

def clamp_pixel(pixel):
    """Same as clamp8, but do it for a triple of three numbers."""
    red, green, blue = pixel
    return (clamp8(red), clamp8(green), clamp8(blue))


def apply_shader(data, shader, *args):
    """Given the data, a shader function, and possibly some additional
    shader parameters, run the shader on each pixel, overwriting the
    data.
    """
    for row in data:
        for i in range(len(row)):
            pixel = row[i]
            
            new_pixel = shader(pixel, *args)
            new_pixel = clamp_pixel(new_pixel)
            
            row[i] = new_pixel


def apply_shader2(data1, data2, shader, *args):
    """Same as apply_shader, but operates on two images of equal
    dimensions and overwrites the first image.
    """
    if not (len(data1) == len(data2) != 0 and
            len(data1[0]) == len(data2[0])):
        raise ValueError('Images must have same dimensions')
    
    for row1, row2 in zip(data1, data2):
        for i in range(len(row1)):
            pixel1 = row1[i]
            pixel2 = row2[i]
            
            new_pixel = shader(pixel1, pixel2, *args)
            new_pixel = clamp_pixel(new_pixel)
            
            row1[i] = new_pixel


def make_shader(f):
    """Make a pixel shader out of an intensity shader."""
    
    def pixshader(pixel, *args):
        red, green, blue = pixel
        return (f(red, *args), f(green, *args), f(blue, *args))
    
    return pixshader


def make_shader2(f):
    """Same as make_shader, but for shaders of two values."""
    
    def pixshader(pixel1, pixel2, *args):
        red1, green1, blue1 = pixel1
        red2, green2, blue2 = pixel2
        return (f(red1, red2, *args), f(green1, green2, *args),
                f(blue1, blue2, *args))
    
    return pixshader


def plot_intshader(intshader, *args):
    """Given an intensity shader, draw a matplotlib plot of its
    output for its entire domain.
    """
    
    import matplotlib.pyplot as plt
    
    xs = range(0, 255)
    plt.plot(xs, [x for x in xs], ':')
    plt.plot(xs, [intshader(x, *args) for x in xs])
    plt.gca().set_xlim(0, 255)
    plt.gca().set_ylim(0, 255)
    plt.show()
