# White tree

'''
    author: grafstor
    date: 12.01.2020

    version 2.0:
        - add C counter
'''

__version__ = "2.0"

from PIL import Image 
import time 
import counter

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

    pixels_vol = counter.count(imgy, imgx, ya, yb, xa, xb, maxIt, rep)

    for y in range(imgy):
        for x in range(imgx): 
            pixels[x, y] = (round(int(pixels_vol[x, y])*0.6),
                            round(int(pixels_vol[x, y])*0.8),
                            round(int(pixels_vol[x, y])*0.9))

    img.save("photo_{0}.png".format(pui),"PNG")

for pui in range(5,6):
    print("Number "+ str(pui))

    main_time = time.time()
    f_mel(1000,1000)
    print(time.time() - main_time)
