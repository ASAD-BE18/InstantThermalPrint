import subprocess
import re


def call_gphoto(arguments):
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


def list_difference(list1, list2):
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

    file_text_block = call_gphoto(["-L", "--new"])  # Get list of new files
    current_files_on_sd = re.finditer("#([0-9]*)\s", file_text_block)
    current_file_list = [matched_item.group(1) for matched_item in current_files_on_sd]

    # Compare this list to the older list to see if new files were added...
    new_file_list = list_difference(current_file_list, old_file_list)
    # Return the numbers of the new files in a list.

    return new_file_list


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
    current_files_on_sd_test = re.finditer("#([0-9]*)\s", test_block)
    current_file_list_test = [matched_item.group(1) for matched_item in current_files_on_sd]



    #get_new_files()
