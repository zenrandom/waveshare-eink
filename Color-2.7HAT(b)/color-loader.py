 #  Author @zenrandom
 #  Based on Demo code from   :   Yehui from Waveshare
 #
 ##

import epd2in7b
import Image
import ImageFont
import ImageDraw
import os, fnmatch

COLORED = 1
UNCOLORED = 0

def main():
    epd = epd2in7b.EPD()
    epd.init()

    frame_black = raw_input("Please name the file you want to draw to screen in black (for a list of files in the current directory enter bmplist): ")

    while frame_black == "bmplist":

        bmpfiles = os.listdir('.')
        pattern = "*.bmp"
        for entry in bmpfiles:
            if fnmatch.fnmatch(entry, pattern):
                print (entry)
        frame_black = raw_input("Please name the file you want to draw to screen in black (for a list of files in the current directory enter bmplist): ")

    frame_red = raw_input("Please name the file you want to draw to screen in red (for a list of files in the current directory enter bmplist): ")

    while frame_red == "bmplist":

        bmpfiles = os.listdir('.')
        pattern = "*.bmp"
        for entry in bmpfiles:
            if fnmatch.fnmatch(entry, pattern):
                print (entry)
        frame_red = raw_input("Please name the file you want to draw to screen in red (for a list of files in the current directory enter bmplist): ")

    background = raw_input("What color do you want to be the background, red or black?")

    # clear the frame buffer
    frame_black = [0] * (epd.width * epd.height / 8)
    frame_red = [0] * (epd.width * epd.height / 8)

    # For simplicity, the arguments are explicit numerical coordinates
    epd.draw_rectangle(frame_black, 10, 130, 50, 180, COLORED);
    epd.draw_line(frame_black, 10, 130, 50, 180, COLORED);
    epd.draw_line(frame_black, 50, 130, 10, 180, COLORED);
    epd.draw_circle(frame_black, 120, 150, 30, COLORED);
    epd.draw_filled_rectangle(frame_red, 10, 200, 50, 250, COLORED);
    epd.draw_filled_rectangle(frame_red, 0, 76, 176, 96, COLORED);
    epd.draw_filled_circle(frame_red, 120, 220, 30, COLORED);

    if background == "black":
    # display images
      frame_black = epd.get_frame_buffer(Image.open('black.bmp'))
      frame_red = epd.get_frame_buffer(Image.open('red.bmp'))
      epd.display_frame(frame_red, frame_black)
    
    elif background == "red":
      frame_black = epd.get_frame_buffer(Image.open('black.bmp'))
      frame_red = epd.get_frame_buffer(Image.open('red.bmp'))
      epd.display_frame(frame_black, frame_red)


    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.IMAGE_BLACK, imagedata.IMAGE_RED)

if __name__ == '__main__':
    main()
