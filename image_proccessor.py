from PIL import Image, ImageEnhance

# Constants:
# resize_size = (1278, 864)  # Original size 5148x3456
resize_size = (852, 576)  # Original size 5148x3456
template_file = "template_file.png"


def adjust_brightness(base_img):
    enhanced = ImageEnhance.Brightness(base_img)
    enhanced.enhance(8)
    return enhanced


def add_logo(base_img, overlay):
    """
    Function to add overlay to the base image.
    :param base_img: path to image.
    :param overlay: path to overlay, png with alpha.
    :return: composite image.
    """
    base_img.paste(overlay, (0, 0), overlay)
    return base_img


def resize_image(base_img):
    """
    Function to resize the base image to the required size.
    :param base_img: path to image.
    :return: resized image.
    """
    base_img = base_img.resize(resize_size)
    return base_img


def process_image(image_path):
    """
    Do the whole processing stage.
        1. Resize
        2. Change brightness and contrast (WIP)
        3. Add the overlay
        4. Return final image.

    :param image_path: path to image.
    :return: Final image.
    """
    output_path = image_path[:-4] + "_edited.png"

    # Open the images
    base_img = Image.open(image_path).resize(resize_size)
    logo = Image.open(template_file)
    # adjusted_image = adjust_brightness(base_img)

    add_logo(base_img, logo)
    base_img.save(output_path)

    return output_path
