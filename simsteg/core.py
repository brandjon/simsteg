# core.py: Image representation, I/O, interface with Pillow.


# Note that this is Pillow, not PIL.
from PIL import Image

# Verbose file I/O.
VERBOSE = True


# We will represent images as a 2-dimensional array whose first index
# indicates the row and whose second index is a column within a row.
# The elements are triples of numbers between 0 and 255, where each
# number represents the Red, Green, and Blue value of that pixel
# respectively. The height of the image is the length of the 2D array,
# and the width is the length of any of its rows. Images with no
# rows are not permitted.

# When we read an image using the Python Imaging Library, the pixel
# data is retrieved as a string of bytes - RGB triplets starting with
# the top left pixel and proceeding left-to-right. The following
# functions convert between that format and ours.


def dataify(strdata, width, height):
    """Given a string of bytes and the image dimensions, turn it into
    a 2D array of pixel triples.
    """
    arr = [ord(c) for c in strdata]
    assert len(arr) % 3 == 0
    
    data = []
    
    for i in range(0, len(arr), 3):
        if (i/3) % width == 0:
            data.append([])
        
        pixel = tuple(arr[i:i+3])
        data[-1].append(pixel)
    
    return data


def stringify(data):
    """Inverse of the dataify function."""
    arr = []
    
    for row in data:
        for pixel in row:
            arr.extend(pixel)
    
    return ''.join(chr(c) for c in arr)


def load_image_data(filename, verbose=VERBOSE):
    """Read in image data from a file and return the pixel data array."""
    
    if verbose:
        print 'Reading image "' + filename + '"'
    
    im = Image.open(filename)
    im = im.convert('RGB')
    width, height = im.size
    data = dataify(im.tostring(), width, height)
    
    if verbose:
        print '  (dimensions: {} x {}; {} pixels)'.format(
            width, height, width * height)
    
    return data


def save_image_data(filename, data, verbose=VERBOSE):
    """Save the pixel data array as an image with the given filename."""
    
    height = len(data)
    assert height > 0
    width = len(data[0])
    string = stringify(data)
    outim = Image.fromstring("RGB", (width, height), string)
    
    if verbose:
        print 'Writing image "' + filename + '"'
    
    outim.save(filename)
