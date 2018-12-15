from stsv.argparser import parse
from stsv.decisions import DecisionCollector, Decision, DecisionExecutionSupervisor
from stsv.file_utils import FileUtils
from stsv.interface import WelcomingInterface


def run():
    extension, resolution_string, pics_directory, selected_dir, discarded_dir = parse()
    collector = DecisionCollector()
    interface = WelcomingInterface(resolution_string)
    decision_key = interface.welcome_and_get_decision_key()

    pictures_paths = FileUtils.list_files_by_extension(extension, pics_directory)
    for i, picture_path in enumerate(pictures_paths):
        caption = "Displaying picture {}. {} of {}".format(picture_path, i + 1, len(pictures_paths))
        interface.display_picture(caption, picture_path)
        decision = interface.await_decision(decision_key, Decision.decision_map())
        collector.record_decision(decision, picture_path)

    interface.clear_screen()

    supervisor = DecisionExecutionSupervisor(pics_directory)
    supervisor.execute(collector, {
        Decision.SELECT: selected_dir,
        Decision.DISCARD: discarded_dir
    })
    print("Finished. Sielo.")
