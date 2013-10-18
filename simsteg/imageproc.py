# imageproc.py: Image processors that are more complex than shaders.


def blur(data, radius):
    """Blur an image by recomputing each pixel as the average of the
    pixels in a neighborhood of a given square radius. A radius of
    size 0 has no effect.
    
    Note that this algorithm is O(m * n * k^2), where m and n are the
    image dimensions and k is the radius.
    """
    
    height = len(data)
    width = len(data[0])
    
    new_data = []
    for i in range(height):
        new_data.append([])
        
        for j in range(width):
            top = max(0, i - radius)
            bottom = min(height - 1, i + radius)
            left = max(0, j - radius)
            right = min(width - 1, j + radius)
            
            rsum, gsum, bsum = 0, 0, 0
            count = 0
            for ni in range(top, bottom+1):
                for nj in range(left, right+1):
                    r, g, b = data[ni][nj]
                    rsum += r
                    gsum += g
                    bsum += b
                    count += 1
            ravg = rsum / count
            gavg = gsum / count
            bavg = bsum / count
            
            avgpixel = (ravg, gavg, bavg)
            
            new_data[-1].append(avgpixel)
    
    data[:] = new_data


def pixelate(data, size):
    """Pixelate an image by dividing it into squares of length
    size, averaging all the pixels in the square, and assigning
    them all this average value.
    """
    
    height = len(data)
    width = len(data[0])
    
    for i in range(0, height, size):
        for j in range(0, width, size):
            bottom = min(height - 1, i + size)
            right = min(width - 1, j + size)
            
            rsum, gsum, bsum = 0, 0, 0
            count = 0
            for ni in range(i, bottom+1):
                for nj in range(j, right+1):
                    r, g, b = data[ni][nj]
                    rsum += r
                    gsum += g
                    bsum += b
                    count += 1
            ravg = rsum / count
            gavg = gsum / count
            bavg = bsum / count
            
            avgpixel = (ravg, gavg, bavg)
            
            for ni in range(i, bottom):
                for nj in range(j, right):
                    data[ni][nj] = avgpixel


def circle(data, radius, color):
    """Draw a circle with the given pixel color over the image."""
    
    height = len(data)
    width = len(data[0])
    
    midy = height/2
    midx = width/2
    
    for i in range(height):
        for j in range(width):
            if (midy - i) ** 2 + (midx - j) ** 2 < radius ** 2:
                data[i][j] = color


def checker(data, color):
    """Draw a checkerboard pattern with the given color over the image
    (effectively dithering).
    """
    
    height = len(data)
    width = len(data[0])
    
    for i in range(height):
        for j in range(width):
            if (i + j) % 2 == 0:
                data[i][j] = color
