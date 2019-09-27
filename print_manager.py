import subprocess
import re
import os

from image_proccessor import *


def _call_gphoto(arguments, shell_usage=False):
    """
    Extend the gphoto2 command with as many arguments as supplied.
    :param arguments: list of arguments.
    :return: output of gphoto2 command
    """
    command = ["gphoto2"]
    command.extend(arguments)
    print(command)
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         shell=shell_usage)
    output, _ = p.communicate()
    return output


def _list_difference(list1, list2):
    """
    Return the difference between list1 and list2 using set.
    :param list1: list1
    :param list2: list2
    :return: list that contains values that are only present in one of the lists.
    """
    list1 = map(str.strip, list1)  # Strip all values in list1
    list2 = map(str.strip, list2)  # Strip all values in list2
    return list(set(list1) - set(list2))


def create_whitelist():
    """
    Function creates whitelist to prevent re-printing.
    """
    with open("whitelist.txt", "w") as whitelist:
        whitelist.write("\n")
        whitelist.close()


def update_whitelist(filename):
    """
    Function that adds the printed files to the whitelist to prevent re-printing.
    """
    with open("whitelist.txt", "a") as whitelist:
        try:
            whitelist.write(str(filename)+"\n")
        finally:
            whitelist.close()


def get_whitelist():
    """
    Function that fetches all files from the whitelist.
    """
    current_whitelist = []
    with open("whitelist.txt", "r") as whitelist:
        try:
            for line in whitelist.readlines():
                current_whitelist.append(line)
        finally:
            whitelist.close()

    return current_whitelist


def get_new_files():
    """
    Function that gets a list of files currently on the SD card of the camera,
    Checks if there are new files and downloads the new files.
    :return: list of new files as numbers i.e: [4,5,6]
    """

    # The text block from the command 'gphoto2 -L --new' will look like this:
    #       #8     IMG_8187.JPG               rd   493 KB image/jpeg
    #       #9     IMG_8188.JPG               rd   496 KB image/jpeg
    # From this list I want to retain the numbers after the pound sign.

    file_text_block = _call_gphoto(["-L", "--new"])  # Get list of new files

    # Parse the output of gphoto2 to get file names and numbers for downloading
    current_files_on_sd = re.finditer(r"#([0-9]+)\s.*(IMG_[0-9]*)+", file_text_block)

    # Hold this data in a dictionary, like so: "9" : "IMG_XYZ.JPG"
    matched_dict = {}
    for matched_thing in current_files_on_sd:
        matched_dict[str(matched_thing.group(1))] = str(matched_thing.group(2)+".JPG")

    # Get current file list and old file lists
    current_file_list = matched_dict.keys()
    old_file_list = get_whitelist()

    # Compare the lists to find the new files
    new_file_list = _list_difference(current_file_list, old_file_list)

    # Create the output dictionary
    output_dict = {}
    for file_id in new_file_list:
        output_dict[str(file_id)] = matched_dict[str(file_id)]

    # Download new files
    for new_file in new_file_list:
        print("Downloading file #" + str(new_file))
        _call_gphoto(["-p", str(new_file).strip()])

    return output_dict


def print_file(image_path):
    p = subprocess.Popen(["lp", "-o", "fit-to-page", image_path],
                         stdout=subprocess.PIPE,
                         shell=False)
    output, _ = p.communicate()
    update_whitelist(image_path)


def remove_file(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)


if __name__ == "__main__":

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
