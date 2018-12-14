import os
from enum import Enum

import cv2
import pkg_resources

from stsv.argparser import parse

MATT = "pics/matt.png"
MATT_PATH = pkg_resources.resource_filename(__name__, MATT)
PICS_DIRECTORY = "."
WAIT_INFINITELY = 0


class Decision(Enum):
    SELECT = 1
    DISCARD = 2


def list_files_in_directory(extension, pictures_directory_path):
    files = [file for file in os.listdir(pictures_directory_path) if file.endswith(extension)]
    return files


def full_path(base, local):
    return "{}/{}".format(base, local)


def create_directory(base, dirname):
    try:
        path = full_path(base, dirname)
        os.makedirs(path)
        return True
    except FileExistsError:
        return False


def move_file_to_directory(base, file, dir_path):
    """
    Yup, ugly as hell, but I don't care. Good enough for now.
    """
    full_file_path = full_path(base, file)
    full_dir_path = full_path(base, dir_path)
    full_new_path = full_path(full_dir_path, file)
    try:
        os.rename(full_file_path, full_new_path)
    except FileNotFoundError:
        pass
        # pass for now


def move_category_to_directory(category_files, target_directory):
    for path in category_files:
        move_file_to_directory(PICS_DIRECTORY, path, target_directory)


def create_and_fill_directory(files, directory_name):
    create_directory(PICS_DIRECTORY, directory_name)
    move_category_to_directory(files, directory_name)


def run():
    extension, selected_dir, discarded_dir = parse()
    pictures_paths = list_files_in_directory(extension, PICS_DIRECTORY)

    print("Press key used for selecting images")
    matt = cv2.imread(MATT_PATH)
    cv2.imshow("Hello there!", matt)
    selector = cv2.waitKey(WAIT_INFINITELY)
    file_decisions = {
        Decision.SELECT: [],
        Decision.DISCARD: []
    }

    for i, picture_path in enumerate(pictures_paths):
        image = cv2.imread(full_path(PICS_DIRECTORY, picture_path))
        caption = "Displaying picture {} of {}".format(i, len(pictures_paths))
        cv2.imshow(caption, image)
        decision = Decision.SELECT if cv2.waitKey(WAIT_INFINITELY) == selector else Decision.DISCARD
        file_decisions[decision].append(picture_path)

    cv2.destroyAllWindows()

    create_and_fill_directory(file_decisions[Decision.SELECT], selected_dir)
    create_and_fill_directory(file_decisions[Decision.DISCARD], discarded_dir)

    create_directory(PICS_DIRECTORY, selected_dir)
    move_category_to_directory(file_decisions[Decision.SELECT], selected_dir)

    create_directory(PICS_DIRECTORY, discarded_dir)
    move_category_to_directory(file_decisions[Decision.DISCARD], discarded_dir)
    print("Finished. Sielo.")
