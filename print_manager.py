import subprocess
import re


def _call_gphoto(arguments):
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
                         shell=False)
    output, _ = p.communicate()
    return output


def _list_difference(list1, list2):
    """
    Return the difference between list1 and list2 using set.
    :param list1: list1
    :param list2: list2
    :return: list that contains values that are only present in one of the lists.
    """
    return list(set(list1) - set(list2))


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
    current_files_on_sd = re.finditer("#([0-9]+)\s.*(IMG_[0-9]*)+", file_text_block)
    output_dict = {}
    for matched_thing in current_files_on_sd:
        output_dict[str(matched_thing.group(1))] = str(matched_thing.group(2)+".JPG")

    current_file_list = output_dict.keys()
    print(current_file_list)

    # Compare this list to the older list to see if new files were added...
    new_file_list = _list_difference(current_file_list, old_file_list)
    # Download new files
    for new_file in new_file_list:
        print("Downloading file " + str(new_file))
        _call_gphoto(["-P", str(new_file)])

    return new_file_list


def update_whitelist():
    """
    Function that adds the printed files to the whitelist to prevent re-printing.
    """
    pass


def add_logo():
    """
    Function that adds the printed files to the whitelist to prevent re-printing.
    """
    pass


def print_file(image_path):
    p = subprocess.Popen(["lp", "-o", "fit-to-page", image_path],
                         stdout=subprocess.PIPE,
                         shell=False)
    output, _ = p.communicate()
    return output
    pass


if __name__ == "__main__":
    old_file_list = []
    # Test code:
    test_block = """
                    #8     IMG_8187.JPG               rd   493 KB image/jpeg
                    #9     IMG_8188.JPG               rd   496 KB image/jpeg
                    #10    IMG_8189.JPG               rd   741 KB image/jpeg
                    #12    IMG_8191.JPG               rd  2912 KB image/jpeg
                    #13    IMG_8192.JPG               rd  2929 KB image/jpeg
                    #14    IMG_8193.JPG               rd  2930 KB image/jpeg
                    #15    IMG_8194.JPG               rd  2924 KB image/jpeg
"""
    t_current_files_on_sd = re.finditer("#([0-9]+)\s.*(IMG_[0-9]*)+", test_block)
    t_output_dict = {}
    for matched_thing in t_current_files_on_sd:
        t_output_dict[str(matched_thing.group(1))] = str(matched_thing.group(2)+".JPG")
    print(t_output_dict)
    current_file_list = list(t_output_dict.keys())
    print(current_file_list)
