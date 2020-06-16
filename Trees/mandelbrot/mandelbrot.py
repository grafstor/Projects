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

def fractal_mndb(size=(100, 100), deep=1, offsets=(0.5,0)):

    pixels = counter.count(size[0], size[1], offsets[0], offsets[1], deep)

    img = Image.fromarray(pixels, 'RGB')
    img.save("photo_deep-{0}.png".format(deep),"PNG")

def main():
    deep = 1
    offsets = (-0.28, .008)

    print("Deep "+ str(deep))

    main_time = time.time()

    fractal_mndb((1500, 1500), deep)

    print(time.time() - main_time)


if __name__ == '__main__':
    main()