def use_remote(
        prompt="Do you want to use a remote tag? (y/n, default no)\n"):
    """
    Returns whether user wants to use a remote tag

    :param str prompt: input prompt,
        "Do you want to use a remote tag? (y/n, default no)" by default
    :return: whether or not to use remote
    :rtype: bool
    """
    to_use_remote = None
    while to_use_remote is None:
        user_input = input(prompt)
        if user_input == "":
            to_use_remote = False
        elif (user_input[0] == "T"
                or user_input[0] == "t"
                or user_input[0] == "y"
                or user_input[0] == "Y"):
            to_use_remote = True
        elif (user_input[0] == "F"
                or user_input[0] == "f"
                or user_input[0] == "N"
                or user_input[0] == "n"):
            to_use_remote = False
    return to_use_remote


def get_remote_id(to_use_remote=True,
                  prompt="Enter remote ID's last 4 digits:\n"):
    """
    Returns desired remote ID from user input

    :param bool to_use_remote: whether to use a remote device
    :param str prompt: input prompt,
        "Enter remote ID's last 4 digits" by default
    :return: remote id
    :rtype: str
    """
    if not to_use_remote:
        return None
    str_last_4_digits = None
    while str_last_4_digits is None or str_last_4_digits.isdigit is False:
        str_last_4_digits = input(prompt)
    return "0x" + str_last_4_digits


def use_file(
        prompt="Do you want to log to a file? (y/n, default no)\n"):
    """
    Returns whether user wants to use a remote tag

    :param str prompt: input prompt,
        "Do you want to use a remote tag? (y/n, default no)" by default
    :return: whether or not to use remote
    :rtype: bool
    """
    to_use_file = None
    while to_use_file is None:
        user_input = input(prompt)
        if user_input == "":
            to_use_file = False
        elif (user_input[0] == "T"
                or user_input[0] == "t"
                or user_input[0] == "y"
                or user_input[0] == "Y"):
            to_use_file = True
        elif (user_input[0] == "F"
                or user_input[0] == "f"
                or user_input[0] == "N"
                or user_input[0] == "n"):
            to_use_file = False
    return to_use_file


def get_filename(to_use_file=True,
                 file_ext=".txt",
                 prompt="Enter filename:\n"):
    """
    Returns desired filename from user input

    :param bool to_use_file: whether to log to a file
    :param str file_ext: file extension, default .txt
    :param str prompt: input prompt, "Enter filename" by default
    :return: filename
    :rtype: str
    """
    if not to_use_file:
        return None
    filename = None
    while filename is None:
        filename = input(prompt)
    return filename + file_ext


def get_attribute_to_log(
        prompt="What do you want to log?\n(pressure, acceleration, magnetic, angular velocity, "
               "euler angles, quaternion, linear acceleration, or gravity)\n"):
    possible_attributes = ["pressure", "acceleration", "magnetic", "angular velocity", "euler angles",
                           "quaternion", "linear acceleration", "gravity"]
    attribute_to_log = ""
    while attribute_to_log not in possible_attributes:  # check if input is correct
        attribute_to_log = input(prompt)
    return attribute_to_log
