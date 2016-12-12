from PIL import Image
# Imports image library stuff
import urllib,io


# Imports libs to read image from internet
import random
# Import sys so we can access argv for command line args
import sys

"""
Class: ImageEdit
Takes an image and depedning on what function is called, 
manipulates the image for each function.
"""
class ImageEdit(object):
    
    def __init__(self,argv):
        
        ## Parse argv that was passed in to our class
        parts = {}
        
        parts['-f'] = argv[2]
        parts['-s'] = argv[4]
        parts['-show'] = True
        parts['method'] = argv[5]

        if '-f' in parts.keys():
            self.input_file = parts['-f']
            self.save_file = self.input_file 
            self.img = Image.open(self.input_file)

        if '-s' in parts.keys():
            self.save_file = parts['-s']
            self.save = True
        else:
            self.save = False

        if '-show' in parts.keys():
            self.show = parts['-show']
            if self.show == "1" or self.show == "True":
                self.show = True
            else:
                self.show = False

        ## Parsing Done!

        # Get width and height of image so we can loop through it
        self.width = self.img.size[0]
        self.height = self.img.size[1]

        # Call local negate method
        if parts['method'] == 'solarize':
            self.solarize()
        if parts['method'] == 'glass_eff':
            self.glass_eff()
        if parts['method'] == 'flip':
            self.flip()
        if parts['method'] == 'poster':
            self.poster()
        # Perform actions based on command line params set above
        if self.save:
            self.img.save(self.save_file)

        if self.show:
            self.img.show()


    # flips the image horizontally
    def flip(self, img=None):
        if not img == None:
            self.img = img
        
        for x in range(self.width):
            for y in range((self.height//2)):
                opposite = self.height - 1 - y
                rgb = self.img.getpixel((x, y))
                rgb2 = self.img.getpixel((x, opposite))
                self.img.putpixel((x, opposite), rgb)
                self.img.putpixel((x, y), rgb2)
        return self.img


    # Attempt at blur function
    #def blur(self, img=None):
    #    if not img == None:
    #        self.img = img
    #    blurring = 5
    #    for x in range(self.width):
    #        for y in range(self.height):
    #            r = 0
    #            g = 0
    #            b = 0
    #            rgb = self.img.getpixel((x, y))
    #            for i in range(blurring):
    #                r += rgb[0]
    #                g += rgb[1]
    #                b += rgb[2]
    #                rgb2 = (r, g, b)
    #            self.img.putpixel((x, y), rgb2)
    #    return self.img

    # Attempt at glass effect
    #def glass_eff(self, img=None):
    #    distance = 5
       
    #    if not img == None:
    #        self.img = img

    #    for x in range(self.width):
    #        nums = [x for x in range(x - distance, x + distance) if (x >= 0 and x<= self.width)]
    #        choicex = random.choice(nums) 
    #        for y in range(self.height):
                
    #            nums2 = [y for y in range(y - distance, y + distance) if (y >= 0 and y <= self.height)]
    #            choicey = random.choice(nums2)
    #            rgb = self.img.getpixel(())
    #            self.img.putpixel((x, y), rgb)


    #    return self.img



     # Negates an image by inverting each pixels color channel
    # If we use  this class as I have it setup now, the input param and return are not used. 
    #
    # Otherwise, we can allow an image to be passed in wich would be negated and returned. 
    # This is how the method would normally be used.
    def solarize(self,img=None):
        if not img == None:
            self.img = img

         # Loop through the image and read every pixel
        for x in range(self.width):
            for y in range(self.height):

                # Get rgb value from pixel
                rgb = self.img.getpixel((x,y))
                
                # Negate each color channel by subtracting it from 255
                rgb2 = (255-rgb[0],255-rgb[1],255-rgb[2])

                # Write the pixel back to the image. This actually
                # is the editing part. Without calling 'putpixel'
                # the image would NOT be changed.
                self.img.putpixel((x,y),rgb2)

        return self.img

    # NOT USED but I left it here 
    def random_color(self):
        return (random.randint(255),random.randint(255),random.randint(255))


# Prints the usage as expected if we don't get enough params
# Remember, we are NOT error checking and in the real world, you MUST!
def print_usage():
    print("Error: \n   Url or filename needed")
    print("Usage: \n   python %s -u url [-o outputfile]\n   python %s -f filename [-s savefile, -show 1]" % (sys.argv[0],sys.argv[0]))
    print("Example: \n   python %s -u https://s-media-cache-ak0.pinimg.com/originals/05/b3/83/05b3831a2cefe769af2e9e5c877e6cc8.jpg -o negative.jpg -show 1" % (sys.argv[0]))
    print("   (this would open the url, process it, save it locally in 'negative.jpg' and also open the result")

# Ummmm run me if this file called directly.
if __name__=='__main__':
    argv = []
    argv.append( 'PythonApplication1.py')
    argv.append('-f')
    argv.append('begonia.jpg')
    argv.append('-s')
    argv.append('begonia_edit.jpg')
    argv.append('poster')

    print(argv)
    neg = ImageEdit(argv)
