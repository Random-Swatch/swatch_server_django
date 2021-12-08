import random
from django.conf import settings


class SwatchGenerator:

    def __init__(self):
        pass

    def generate(self):
        color = []
        for _ in range(settings.SWATCH_SIZE):
            random_space = settings.SWATCH_COLOR_SPACES[random.randint(0, len(settings.SWATCH_COLOR_SPACES) - 1)]
            color.append(random_space().generate())
        return color
