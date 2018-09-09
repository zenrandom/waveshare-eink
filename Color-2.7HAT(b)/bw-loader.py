##
 #  @filename   :   main.cpp
 #  @brief      :   2.7inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     August 16 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

import epd2in7b
import Image
import ImageFont
import ImageDraw
import os, fnmatch


def main():
    epd = epd2in7b.EPD()
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
    image = Image.new('1', (epd2in7b.EPD_WIDTH, epd2in7b.EPD_HEIGHT), 255)    # 255: clear the image with white
    draw = ImageDraw.Draw(image)

    epd.display_frame(epd.get_frame_buffer(image))

    # display images
    epd.display_frame(epd.get_frame_buffer(Image.open(imagefile)))

if __name__ == '__main__':
    main()
