from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        return self.image

    def add_text_variant_1(self):
        draw = ImageDraw.Draw(self.image)
        text = "Вариант 1"

        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        width, height = self.image.size

        x = width - text_width - 10
        y = height - text_height - 10

        draw.text((x, y), text, font=font, fill=(255, 255, 255))

        return self.image
