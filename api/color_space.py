import random

from api.color import Color


class ColorSpace:

    def __init__(self):
        pass

    # This method returns the color space type.
    # RGB, HSL
    def get_type(self):
        pass

    # This method should return the syntax to use the color in Web UI.
    # Ex: "hsl(29, 88%, 33%)"
    def get_syntax(self):
        pass

    #  This method should return the CSS compatibility status of the color space.
    #  Ex: If the color space is compatible with the latest CSS version,
    #  this value should be `true` else, should be `false`.
    def get_is_css_compatible(self):
        pass

    # This method should generate a random color from the space.
    # And should return an object of the api.color.Color class
    def generate(self):
        pass


class RgbSpace(ColorSpace):

    def __init__(self):
        super().__init__()
        self.red = 0
        self.green = 0
        self.blue = 0

    def get_type(self):
        return "RGB"

    def get_syntax(self):
        return "rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"

    def get_is_css_compatible(self):
        return True

    def generate(self):
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        return Color(self.get_type(), self.get_syntax(), self.get_is_css_compatible())


class HslSpace(ColorSpace):

    def __init__(self):
        super().__init__()
        self.hue = 0
        self.saturation = 0
        self.lightness = 0

    def get_type(self):
        return "HSL"

    def get_syntax(self):
        return "hsl(" + str(self.hue) + ", " + str(self.saturation) + "%, " + str(self.lightness) + "%)"

    def get_is_css_compatible(self):
        return True

    def generate(self):
        self.hue = random.randint(0, 359)
        self.saturation = random.randint(0, 100)
        self.lightness = random.randint(0, 100)
        return Color(self.get_type(), self.get_syntax(), self.get_is_css_compatible())
