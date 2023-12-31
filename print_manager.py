import os
from picamera import PiCamera
from time import sleep
from image_proccessor import *

def capture_image(image_path):
    """
    Capture an image using PiCamera and save it to the specified path.
    :param image_path: path to save the image
    :return: Nothing
    """
    camera = PiCamera()
    camera.start_preview()
    sleep(5)  # Allow time for the camera to warm up
    camera.capture(image_path)
    camera.stop_preview()

def get_new_files():
    """
    Function that captures a new image and returns the file path.
    :return: path of the new image
    """
    image_path = "/path/to/save/image.jpg"  # Specify the path to save the image
    capture_image(image_path)
    return {1: image_path}

def queue_and_print(channel=None):
    if not os.path.exists("whitelist.txt"):
        create_whitelist()

    downloaded_images_dict = get_new_files()

    for image in downloaded_images_dict:
        # Do some processing on the image
        processed_img = process_image(downloaded_images_dict[image])

        # Print the image
        print_file(processed_img)

        # Remove the original file as it is not useful anymore
        remove_file(downloaded_images_dict[image])
