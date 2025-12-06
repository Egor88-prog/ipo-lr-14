from image.imagehandler import ImageHandler


def main():
    handler = ImageHandler("image_2.jpg")
    handler.load_image()
    handler.resize_300()

    processor = handler.get_processor()
    processed = processor.apply_blur()
    processed = processor.add_text_variant_1()

    handler.image = processed 

    handler.save_png("output.png")


if __name__ == "__main__":
    main()
