import os


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
