"""A program that encodes and decodes hidden messages in images through LSB steganography"""
from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="images/encoded_sample.png"):
    """Decodes the hidden message in an image

    file_location: the location of the image file to decode. By default is the provided encoded image in the images folder
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    red_loaded = red_channel.load()

    #parsing through the image pixels
    for row in range(x_size):
        for col in range(y_size):
            #finding the red channel of a pixel
            red_pixel = red_loaded[row,col]
            #converting it into an integer
            red_pixel= int(red_pixel)
            #finding the LSB
            red_pixel = red_pixel & 1
            #if its 0, we get white, if it's 1, we get black
            if red_pixel == 0:
                red_pixel = (255,255,255)
            else:
                red_pixel = (0,0,0)
            #putting it back into the image
            pixels[row,col]= red_pixel

    decoded_image.save("images/decoded_image3.png")


def write_text(text_to_write, image_size):
    """Writes text to an RGB image. Automatically line wraps

    text_to_write: the text to write to the image
    image_size: size of the resulting text image. Is a tuple (x_size, y_size)
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    #Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encode_image(text_to_encode= 'SURPRISE!!', template_image="images/samoyed.jpg"):
    """Encodes a text message into an image

    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    encoded_image = Image.open(template_image)
    red_channel = encoded_image.split()[0]
    red_loaded = red_channel.load()

    image_text = write_text("SURPRISE!!", encoded_image.size)
    pixels = image_text.load()
    image_text.save("images/image_text.png")
    #encode_pixels= encode_image.load()

    x_size = image_text.size[0]
    y_size = image_text.size[1]

    for row in range(x_size):
        for col in range(y_size):
            red_pix = red_loaded[row,col]
            #checking to see if the pixel from word file is black
            if pixels[row,col] == (0,0,0):
                #if it is, and if the last bit of the red column is 1, then it will take its complement
                if red_pix & 1 == 1:
                    new_pix[row,col]
                    red_pix = red_pix & ~1
            # checks to see if the pixel is white
            elif pixels[row,col] == (255,255,255):
                #if the last bit of the red column is 0, then takes the complement
                if red_pix & 1 == 0:
                    red_pix= red_pix | 1
            #saves everything and loads it
            red_loaded[row,col] = red_pix
        encoded_image.save("images/index.png")

if __name__ == '__main__':
    #print("Decoding the image...")
    decode_image("images/index.png")

    #print("Encoding the image...")
    encode_image(template_image="images/index.png")
