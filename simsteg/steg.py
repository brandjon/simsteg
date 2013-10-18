# steg.py: Steganography routines.


from core import VERBOSE, load_image_data, save_image_data
from shader import make_shader, make_shader2


def int_xor(v1, v2):
    return v1 ^ v2

def int_shrink_to(v, k):
    """Bit shift right to fit the pixel data within the k
    least-significant bits, truncating as needed and leaving
    the upper bit positions 0.
    """
    return v >> (8 - k)

def int_expand_from(v, k):
    """Bit shift left to make the k least-significant bits
    the most-significant, overwriting the existing upper bit
    positions and leaving the lower bit positions 0.
    """
    return (v << (8 - k)) & 0xFF

def int_noisyexpand_from(v, k):
    """Same as above, but fill the lower bit positions with noise."""
    from random import getrandbits
    r = getrandbits(8 - k) if 8 - k != 0 else 0
    e = (v << (8 - k)) & 0xFF
    return e | r


xor = make_shader2(int_xor)
shrink_to = make_shader(int_shrink_to)
expand_from = make_shader(int_expand_from)
noisyexpand_from = make_shader(int_noisyexpand_from)


def hide(carrier, signal, k):
    """Hide the upper k bits of signal in the lower k bits of carrier."""
    from shader import apply_shader, apply_shader2
    from sample_shaders import flatten
    
#     print 'signal: ' + ', '.join(format(c, '0>8b') for c in signal[0][0])
    
    apply_shader(signal, shrink_to, k)
#     print 'signal: ' + ', '.join(format(c, '0>8b') for c in signal[0][0])
#     print 'carrier: ' + ', '.join(format(c, '0>8b') for c in carrier[0][0])
    apply_shader(carrier, flatten, k)
#     print 'carrier: ' + ', '.join(format(c, '0>8b') for c in carrier[0][0])
    apply_shader2(carrier, signal, xor)
#     print 'carrier: ' + ', '.join(format(c, '0>8b') for c in carrier[0][0])

# Retrieve the lower k bits from the combined image, , overwriting the combined contents.
def unhide(data, k):
    """Unhide the image stored in the lower k bits of the data,
    overwriting the carrier image and filling the low bit positions
    with random noise.
    """
    from shader import apply_shader
    apply_shader(data, expand_from, k)


def do_hide(carrier, signal, out, k, verbose=VERBOSE):
    c_im = load_image_data(carrier)
    s_im = load_image_data(signal)
    
    if VERBOSE:
        print 'Processing...'
    hide(c_im, s_im, k)
    
    save_image_data(out, c_im)

def do_unhide(message, out, k):
    m_im = load_image_data(message)
    
    if VERBOSE:
        print 'Processing...'
    unhide(m_im, k)
    
    save_image_data(out, m_im)
