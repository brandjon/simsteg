# main.py: Main file for running image transformations.


# TO USE: Place a bitmap named "in.bmp" in the image/ directory.
#         Uncomment one or more of the processing lines below
#         and use different values for the val variable to control
#         how the image is distorted. Output is written to
#         "image/out.bmp".
#
#         Uncomment the plot_intshader lines to see a graph of
#         the intshader's output value versus the input intensity. 


from simsteg.core import load_image_data, save_image_data
from simsteg.shader import apply_shader, make_shader, plot_intshader
from simsteg.sample_shaders import *
from simsteg.imageproc import *


prefix = 'image/'


data = load_image_data(prefix + 'in.bmp')
print 'Processing...'


# Uncomment the appropriate lines to test one or more shaders or
# processors.

# Experiment with different values for val.
val = 1

# apply_shader(data, brighten, val)
# apply_shader(data, contrast, val)
# apply_shader(data, gamma, val)

# apply_shader(data, addnoise, val)
# apply_shader(data, flatten, val)

# apply_shader(data, random_grey)
# apply_shader(data, random_color)
# apply_shader(data, swap_colors)
# apply_shader(data, invert)

# blur(data, val)
# pixelate(data, val)

#circle(data, val, (0, 255, 255))
#checker(data, (0, 255, 0))

save_image_data(prefix + 'out.bmp', data)

print 'Done'


# Uncomment to use matplotlib to draw a plot of these functions.

# plot_intshader(int_brighten, val)
# plot_intshader(int_contrast, val)
# plot_intshader(int_gamma, val)
# plot_intshader(int_addnoise, val)
# plot_intshader(int_flatten, val)
