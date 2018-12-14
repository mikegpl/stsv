import os
import cv2
import pkg_resources

from stsv.file_utils import FileUtils
from stsv.argparser import parse
from stsv.decisions import DecisionExecutor, DecisionCollector, Decision
from stsv.interface import Interface

MATT = os.path.join("pics", "matt.png")
MATT_PATH = pkg_resources.resource_filename(__name__, MATT)


def run():
    interface = Interface()
    extension, pics_directory, selected_dir, discarded_dir = parse()
    pictures_paths = FileUtils.list_files_by_extension(extension, pics_directory)

    interface.display_picture("Hello there", cv2.imread(MATT_PATH))
    print("Press key used for selecting images")

    selector = interface.get_keystroke()
    collector = DecisionCollector()

    for i, picture_path in enumerate(pictures_paths):
        caption = "Displaying picture {}. {} of {}".format(picture_path, i, len(pictures_paths))
        Interface.display_picture(caption, cv2.imread(picture_path))
        decision = Interface.get_decision(selector, Decision.SELECT, Decision.DISCARD)
        collector.make_decision(decision, picture_path)

    Interface.clear_screen()
    executor_selected = DecisionExecutor(pics_directory, collector.selected(), Decision.dir_for_enum(Decision.SELECT))
    executor_discarded = DecisionExecutor(pics_directory, collector.discarded(),
                                          Decision.dir_for_enum(Decision.DISCARD))

    executor_selected.move_category_to_directory()
    executor_discarded.move_category_to_directory()
    print("Finished. Sielo.")
