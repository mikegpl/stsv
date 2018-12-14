import os
from enum import Enum

import cv2
import pkg_resources

from stsv.argparser import parse

MATT = os.path.join("pics", "matt.png")
MATT_PATH = pkg_resources.resource_filename(__name__, MATT)
PICS_DIRECTORY = "."
WAIT_INFINITELY = 0


class Decision(Enum):
    SELECT = 1
    DISCARD = 2

    @staticmethod
    def dir_for_enum(enum):
        dirs = {Decision.SELECT: "selected",
                Decision.DISCARD: "discarded"}
        return dirs[enum]


class FileUtils:
    @staticmethod
    def list_files_by_extension(extension, directory_path):
        files = [file for file in os.listdir(directory_path) if file.endswith(extension)]
        return files

    @staticmethod
    def full_path(base, local):
        return os.path.join(base, local)

    @staticmethod
    def create_directory(base, dirname):
        try:
            path = FileUtils.full_path(base, dirname)
            os.makedirs(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def move_file_to_directory(base_path, file_name, directory_name):
        """
        Yup, ugly as hell, but I don't care. Good enough for now.
        """
        path = FileUtils.full_path

        full_file_path = path(base_path, file_name)
        full_dir_path = path(base_path, directory_name)
        full_new_path = path(full_dir_path, file_name)
        try:
            os.rename(full_file_path, full_new_path)
        except FileNotFoundError:
            pass
            # pass for now


class DecisionExecutor:
    def __init__(self, base_directory, category_filenames, target_directory_name):
        self.base_directory = base_directory
        self.category_filenames = category_filenames
        self.target_directory_name = target_directory_name

    def move_category_to_directory(self):
        print("MUWING")
        print(self.category_filenames)
        self._create_and_fill_directory()
        for path in self.category_filenames:
            FileUtils.move_file_to_directory(self.base_directory, path, self.target_directory_name)

    def _create_and_fill_directory(self):
        FileUtils.create_directory(self.base_directory, self.target_directory_name)


class Interface:
    @staticmethod
    def display_picture(caption, image):
        cv2.destroyAllWindows()
        cv2.imshow(caption, image)

    @staticmethod
    def get_decision(selector):
        return Decision.SELECT if Interface.get_keystroke(WAIT_INFINITELY) == selector else Decision.DISCARD

    @staticmethod
    def get_keystroke(timeout):
        return cv2.waitKey(timeout)

    @staticmethod
    def clear_screen():
        cv2.destroyAllWindows()


class DecisionCollector:
    def __init__(self):
        self.file_decisions = {
            Decision.SELECT: [],
            Decision.DISCARD: []
        }

    def make_decision(self, decision, filename):
        self.file_decisions[decision].append(filename)

    def selected(self):
        return self.file_decisions[Decision.SELECT]

    def discarded(self):
        return self.file_decisions[Decision.DISCARD]


def run():
    interface = Interface()
    extension, selected_dir, discarded_dir = parse()
    pictures_paths = FileUtils.list_files_by_extension(extension, PICS_DIRECTORY)

    interface.display_picture("Hello there", cv2.imread(MATT_PATH))
    print("Press key used for selecting images")

    selector = interface.get_keystroke(WAIT_INFINITELY)
    collector = DecisionCollector()

    for i, picture_path in enumerate(pictures_paths):
        caption = "Displaying picture {} of {}".format(i, len(pictures_paths))
        Interface.display_picture(caption, cv2.imread(picture_path))
        decision = Interface.get_decision(selector)
        collector.make_decision(decision, picture_path)

    Interface.clear_screen()
    executor_selected = DecisionExecutor(PICS_DIRECTORY, collector.selected(), Decision.dir_for_enum(Decision.SELECT))
    executor_discarded = DecisionExecutor(PICS_DIRECTORY, collector.discarded(),
                                          Decision.dir_for_enum(Decision.DISCARD))

    executor_selected.move_category_to_directory()
    executor_discarded.move_category_to_directory()
    print("Finished. Sielo.")
