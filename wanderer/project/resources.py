from PIL import Image, ImageTk


class Resources:

    def __init__(self):
        self.images = {}
        self.images['floor'] = self.load_image('project/assets/floor.gif')
        self.images['wall'] = self.load_image('project/assets/wall.gif')
        self.images['Boss'] = self.load_image('project/assets/boss.gif')
        self.images['Skeleton'] = self.load_image(
            'project/assets/skeleton.gif')
        self.images['hero-down'] = self.load_image(
            'project/assets/hero-down.gif')
        self.images['hero-left'] = self.load_image(
            'project/assets/hero-left.gif')
        self.images['hero-right'] = self.load_image(
            'project/assets/hero-right.gif')
        self.images['hero-up'] = self.load_image('project/assets/hero-up.gif')
        self.floor_size = self.images['floor'].width()

    def load_image(self, path):
        return ImageTk.PhotoImage(Image.open(path))

    def get_image(self, key):
        return self.images[key]
