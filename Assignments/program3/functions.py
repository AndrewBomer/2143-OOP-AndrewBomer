def glass_eff(self, img=None):
        distance = 5
       
        if not img == None:
            self.img = img

        for x in range(self.width):
            nums = [x for x in range(x - distance, x + distance) if (x >= 0 and x<= self.width)]
            choicex = random.choice(nums) 
            for y in range(self.height):
                
                nums2 = [y for y in range(y - distance, y + distance) if (y >= 0 and y <= self.height)]
                choicey = random.choice(nums2)
                rgb = self.img.getpixel(())
                self.img.putpixel((x, y), rgb)


        return self.img
        
def blur(self, img=None):
        if not img == None:
            self.img = img
        blurring = 5
        for x in range(self.width):
            for y in range(self.height):
                r = 0
                g = 0
                b = 0
                rgb = self.img.getpixel((x, y))
                for i in range(blurring):
                    r += rgb[0]
                    g += rgb[1]
                    b += rgb[2]
                    rgb2 = (r, g, b)
                self.img.putpixel((x, y), rgb2)
        return self.img
