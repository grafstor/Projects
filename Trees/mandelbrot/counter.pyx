import numpy as np

def count(int imgy, int imgx, float ya, float yb,  float xa,  float xb, int maxIt, int rep):
    cdef int y, x, i
    cdef float zx, zy
    cdef complex z, c

    cdef pixels = np.zeros([imgx, imgy])

    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1)  + ya 
        for x in range(imgx): 
            zx = x * (xb - xa) / (imgx - 1)  + xa

            z = zx + zy * 1j
            c = z

            for i in range(maxIt): 
                if abs(z) > 2.0:
                    break
                z = z * z + c 

            if i == maxIt-1:
                pixels[x, y] = 0
            else:
                if i%255 == 0:
                    rep+=1

                if rep%2:
                    pixels[x, y] = 255 - i%255
                else:
                    pixels[x, y] = i%255
                                  
    return pixels