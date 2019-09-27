from PIL import Image, ImageEnhance

# Constants:
resize_size = (1278, 864)  # Original size 5148x3456
template_file = "template_file.png"


def adjust_brightness(base_img):
    enhanced = ImageEnhance.Brightness(base_img)
    enhanced.enhance(8)
    return enhanced


def add_logo(base_img, overlay):
    """
    Function that adds logo\watermark to the camera pictures
    """
    base_img.paste(overlay, (0, 0), overlay)
    return base_img


def resize_image(base_img):
    base_img = base_img.resize(resize_size)
    return base_img


def process_image(image_path):
    output_path = image_path[:-4] + "_edited.png"

    # Open the images
    base_img = Image.open(image_path).resize(resize_size)
    logo = Image.open(template_file)
    # adjusted_image = adjust_brightness(base_img)

    add_logo(base_img, logo)
    base_img.save(output_path)

    return output_path


if __name__ == "__main__":
    # Don't call this
    pass
