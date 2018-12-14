from stsv.argparser import parse
from stsv.decisions import DecisionCollector, Decision, DecisionExecutionSupervisor
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
        collector.record_decision(decision, picture_path)

    Interface.clear_screen()

    supervisor = DecisionExecutionSupervisor(pics_directory)
    supervisor.execute(collector, {
        Decision.SELECT: selected_dir,
        Decision.DISCARD: discarded_dir
    })
    print("Finished. Sielo.")
