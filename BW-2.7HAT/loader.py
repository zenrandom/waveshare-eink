##  author @zenrandom
 #  based on code:  Yehui from Waveshare
 ##

import epd2in7
import Image
import ImageFont
import ImageDraw
import os, fnmatch


def main():
    epd = epd2in7.EPD()
    epd.init()


    imagefile= raw_input("Please name the file you want to draw to screen (for a list of files in the current directory enter bmplist): ")

    while imagefile == "bmplist":

        bmpfiles = os.listdir('.')
        pattern = "*.bmp"
        for entry in bmpfiles:
            if fnmatch.fnmatch(entry, pattern):
                print (entry)
        imagefile= raw_input("Please name the file you want to draw to screen (for a list of files in the current directory enter bmplist): ")



    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)    # 255: clear the image with white
    draw = ImageDraw.Draw(image)

    epd.display_frame(epd.get_frame_buffer(image))

    # display images
    epd.display_frame(epd.get_frame_buffer(Image.open(imagefile)))

if __name__ == '__main__':
    main()
