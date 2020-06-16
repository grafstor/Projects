from numpy import zeros, array, uint8

def count(int size_x, int size_y, float offset_x, float offset_y, int deep):
    cdef int y, x, i, maxIt, rep
    cdef float zx, zy, ya, yb, xa, xb
    cdef complex z, c

    rep = 0

    xa = -1.0 / deep**(0.9*deep) - offset_x
    xb = 1.0 / deep**(0.9*deep) - offset_x
    ya = -1.0 / deep**(0.9*deep) - offset_y
    yb = 1.0 / deep**(0.9*deep) - offset_y

    maxIt =  100 + (deep*(deep**2))

    xui = 455 / maxIt

    cdef pixels = zeros([size_x, size_y, 3], dtype=uint8)

    for y in range(size_y):
        zy = y * (yb - ya) / (size_y - 1)  + ya 
        for x in range(size_x):
            zx = x * (xb - xa) / (size_x - 1)  + xa

            z = zx + zy * 1j
            c = z

            for i in range(maxIt): 
                if abs(z) > 2.0:
                    break
                z = z * z + c 

            if i == maxIt-1:
                pixels[y, x] = [0, 0, 0]

            else:
                if i%255 == 0:
                    rep+=1

                if rep%2:
                    pixels[y, x] = [(255-i%255)*0.6, (255-i%255)*0.8, (255-i%255)*0.9]

                else:
                    pixels[y, x] = [(i%255)*0.6, (i%255)*0.8, (i%255)*0.9]
                                  
    return pixels