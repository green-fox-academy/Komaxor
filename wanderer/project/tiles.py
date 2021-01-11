from PIL import Image, ImageTk

class Tile:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.has_monster = False
        self.has_hero = False
        self.walkable = False
        self.image_path = ""

    def get_image(self):
        return ImageTk.PhotoImage(Image.open(self.image_path))
