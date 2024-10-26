"""EX06: Practice with Dictionary Util Functions."""

__author__ = "730649404"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Switches keys and values of a dict"""
    invert_dict: dict[str, str] = {}
    # makes empty dict
    value_list: list[str] = []
    # makes empty list to check for duplicate values
    for key in input_dict:
        for idx in range(0, len(value_list)):
            if value_list[idx] == input_dict[key]:
                # if there are mulitple of the same value
                raise KeyError("Duplicate values in list!")
                # since keys can not be the same
        value_list.append(input_dict[key])
        # adds value to list to be compared by future values
    for key in input_dict:
        new_key: str = input_dict[key]
        # takes value of key of input_dict
        invert_dict[new_key] = key
        # makes value into key
    return invert_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds color that appears most frequently"""
    color_total: dict[str, int] = {}
    # dict keeps track of total of each color
    freq_color: str = ""
    # what color is listed the most
    count: int = 0
    # keeps track of amount of most frequent color
    for person in color_dict:
        color: str = color_dict[person]
        # finds color
        color_total[color] = 0
        # adds color starting at count 0
        color_total[color] += 1
        # adds one to count of color in dict
    for color in color_total:
        if color_total[color] > count:
            # if valoue of dict is greater than previous max
            count = color_total[color]
            # updates to most frequent color
            freq_color = color
    return freq_color


def count(str_list: list[str]) -> dict[str, int]:
    """Makes dict that makes count of strings from the key"""
    count_dict: dict[str, int] = {}
    # empty dict to keep track of count of strings from the key
    for string in str_list:
        if string in count_dict:
            count_dict[string] += 1
            # adds one to count in dict of it already is in dict
        else:
            count_dict[string] = 1
            # starts count at one for new str
    return count_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Makes dict of words that start with a correspoding letter"""
    alphabetized_dict: dict[str, list[str]] = {}
    # empty dict that words corresponding with letters will be entered
    for word in input_list:
        lower_first_letter: str = word[0].lower()
        # makes first letter fo str lower case
        if lower_first_letter in alphabetized_dict:
            # checks if key exists in existing list
            alphabetized_dict[lower_first_letter].append(word)
            # adds word to list in corresponding letter key
        else:
            # if letter has not been added to list yet
            alphabetized_dict[lower_first_letter] = [word]
            # makes a list for the corresponding letter in dict
    return alphabetized_dict


def update_attendance(
    attendance_log: dict[str, list[str]], day_of_week: str, student: str
) -> None:
    """Updates dictionary to reflect attendence of students (dow for student)"""
    if day_of_week in attendance_log:
        # if day of week is already in dict
        if student in attendance_log[day_of_week]:
            student = student
            # skips if statement
        else:
            attendance_log[day_of_week].append(student)
            # adds student to existing list in dict
    else:
        attendance_log[day_of_week] = [student]
        # makes new key for day of week and value of student name
