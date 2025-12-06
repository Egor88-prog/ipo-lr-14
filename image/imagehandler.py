
from PIL import Image
from .imageprocessor import ImageProcessor

class ImageHandler:
    def __init__(self, path: str):
        self.path = path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.path)
        return self.image

    def resize_300(self):
        if self.image is None:
            raise ValueError("Image not loaded.")
        self.image = self.image.resize((300, 300))
        return self.image

    def save_png(self, output_path: str):
        if self.image is None:
            raise ValueError("Image not loaded.")
        self.image.save(output_path, format="PNG")

    def get_processor(self):
        if self.image is None:
            raise ValueError("Image not loaded.")
        return ImageProcessor(self.image)
