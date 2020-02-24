# White tree

'''
    author: grafstor
    date: 12.01.2020
'''

__version__ = "1.0"

from PIL import Image 
import time

def f_mel(imgx=100,imgy=100):
    sdvig_x = -0.28
    sdvig_y = .008

    xa = -1.0 / pui**(0.9*pui) - sdvig_x
    xb = 1.0 / pui**(0.9*pui) - sdvig_x
    ya = -1.0 / pui**(0.9*pui) - sdvig_y
    yb = 1.0 / pui**(0.9*pui) - sdvig_y

    maxIt =  100 + (pui*(pui**2))
    
    xui = 455 / maxIt

    img = Image.new("RGB", (imgx, imgy))
    pixels = img.load() 
    rep = 0
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
                pixels[x, y] = (0, 0, 0)
            else:
                # pixels[x, y] = (round(i*xui),
                #               round(i*xui),
                #               round(i*xui))
                if i%255 == 0:
                    rep+=1

                if rep%2:
                    pixels[x, y] = (round(255 - i%255*0.6),
                                    round(255 - i%255*0.8),
                                    round(255 - i%255*0.9))
                else:
                    pixels[x, y] = (round(i%255*0.6),
                                    round(i%255*0.8),
                                    round(i%255*0.9))
    img.save("photo_{0}.png".format(pui),"PNG")

for pui in range(5,6):
    print("Number "+ str(pui))
    main_time = time.time()
    f_mel(300,300)
    print(time.time() - main_time)
