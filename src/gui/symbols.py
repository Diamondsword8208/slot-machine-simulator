class Symbol:
    def __init__(self, name, image_path):
        self.name = name
        self.image_path = image_path

    def load_image(self):
        # Logic to load the symbol's image from the image_path
        pass

    def __str__(self):
        return self.name