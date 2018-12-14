from stsv.argparser import parse
from stsv.decisions import DecisionExecutor, DecisionCollector, Decision
from stsv.file_utils import FileUtils
from stsv.interface import Interface, WelcomingInterface


def run():
    extension, pics_directory, selected_dir, discarded_dir = parse()
    selector = WelcomingInterface().welcome_and_get_decision_key()
    collector = DecisionCollector()

    pictures_paths = FileUtils.list_files_by_extension(extension, pics_directory)
    for i, picture_path in enumerate(pictures_paths):
        caption = "Displaying picture {}. {} of {}".format(picture_path, i, len(pictures_paths))
        Interface.display_picture(caption, picture_path)
        decision = Interface.get_decision(selector, Decision.decision_map())
        collector.make_decision(decision, picture_path)

    Interface.clear_screen()
    executor_selected = DecisionExecutor(pics_directory, collector.selected(), Decision.dir_for_enum(Decision.SELECT))
    executor_discarded = DecisionExecutor(pics_directory, collector.discarded(),
                                          Decision.dir_for_enum(Decision.DISCARD))

    executor_selected.move_category_to_directory()
    executor_discarded.move_category_to_directory()
    print("Finished. Sielo.")
