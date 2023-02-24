# Note to self: Do not use transparent images.
# ALWAYS have an image copied when starting the script.
# Set the pen size to the lowest size






size = [20, 20] #Size of the image you draw, in pixels. Try and keep this low because the larger the image the longer it takes to draw.
# Often 20x20 images don't finish drawing, but most of the time they're close AND somewhat understandable so good enough.



































import mouse
import pyautogui
from PIL import *
from PIL import ImageGrab
from PIL import Image
import cv2
from time import *
#Black: 1479, 277
#Green :1479, 357
#White: 1547, 277
#x distance between colors: 68

#top left: 279. 319
#bottom right: 1184, 952

#smallest pen size: 1491 486

#canvas size: 905, 633
sleep(3)

color2Pos = {
    "0,0,0":[1479+(0*68), 277],
    "255,255,255":[1479+(1*68), 277],
    "193,193,193":[1479+(2*68), 277],
    "239,19,11":[1479+(3*68), 277],
    "255,113,0":[1479+(4*68), 277],
    "255,228,0":[1479+(5*68), 277],
    "1,178,255":[1479+(5*68), 277],
    "0,204,0":[1479+(0*68), 340],
    "35,31,211":[1479+(1*68), 340],
    "16,19,186":[1479+(2*68), 340],
    "163,0,186":[1479+(3*68), 340],
    "211,124,170":[1479+(4*68), 340],
    "160,82,45":[1479+(5*68), 340]
}

palette_path = "C:\\Users\\rando\\OneDrive\\Documents\\gimkit palette.png"
output_path = "C:\\Users\\rando\\OneDrive\\Documents\\output.png"
im = ImageGrab.grabclipboard()
im = im.resize(size)
palette = Image.open(palette_path)
im = im.quantize(12, 0, palette=palette, dither=1)
im.save(output_path)
pixels = cv2.imread(output_path)
p_prev = [999, 999, 999]
for y in range(im.height-1):
    for x in range(im.width-1):
        p = pixels[y][x]
        if not (p_prev[0] == p[0] and p_prev[1] == p[1] and p_prev[2] == p[2]):
            try:
                pos = color2Pos.get(str(p[2]) + "," + str(p[1]) + "," + str(p[0]))
                pyautogui.moveTo(pos[0], pos[1])
                mouse.click()
            except:
                print("error selecting color " + str(p))
        p_prev = p
        #sleep(0)
        mouse.move(((279 + (x*5))*1), (319+(y*5))*1)
        mouse.click()
        sleep(.025)
        
