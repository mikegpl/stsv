from enum import Enum
from stsv.file_utils import FileUtils


class Decision(Enum):
    SELECT = 1
    DISCARD = 2

    @staticmethod
    def decision_map():
        return {True: Decision.SELECT,
                False: Decision.DISCARD}


class DecisionExecutor:
    def __init__(self, base_directory, category_filenames, target_directory_name):
        self.base_directory = base_directory
        self.category_filenames = category_filenames
        self.target_directory_name = target_directory_name

    def move_category_to_directory(self):
        self._create_and_fill_directory()
        for path in self.category_filenames:
            FileUtils.move_file_to_directory(self.base_directory, path, self.target_directory_name)

    def _create_and_fill_directory(self):
        FileUtils.create_directory(self.base_directory, self.target_directory_name)


class DecisionCollector:
    def __init__(self):
        self.file_decisions = {
            Decision.SELECT: [],
            Decision.DISCARD: []
        }

    def record_decision(self, decision, filename):
        self.file_decisions[decision].append(filename)

    def files_for_decision(self, decision):
        return self.file_decisions[decision]


class DecisionExecutionSupervisor:
    def __init__(self, base_directory):
        self.base_directory = base_directory

    def execute(self, collector, decision_to_directory):
        for decision, directory in decision_to_directory.items():
            executor = DecisionExecutor(self.base_directory, collector.files_for_decision(decision), directory)
            executor.move_category_to_directory()
