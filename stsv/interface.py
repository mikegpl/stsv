import cv2
import os
import pkg_resources

MATT = os.path.join("pics", "matt.png")
MATT_PATH = pkg_resources.resource_filename(__name__, MATT)


class Interface:
    WAIT_INFINITELY = 0
    RESOLUTION_SEPARATOR = 'x'

    def __init__(self, resolution_string):
        [self.screen_width, self.screen_height] = [int(n) for n in
                                                   resolution_string.split(Interface.RESOLUTION_SEPARATOR)]

    def display_picture(self, caption, image_path):
        cv2.destroyAllWindows()
        cv2.namedWindow(caption, cv2.WINDOW_NORMAL)

        picture = cv2.imread(image_path)
        scaled_width, scaled_height = self.scaled_to_screen_picture_size(picture)
        cv2.resizeWindow(caption, scaled_width, scaled_height)
        cv2.imshow(caption, picture)

    def scaled_to_screen_picture_size(self, image):
        shape = image.shape
        width, height = shape[1], shape[0]

        scale = 1.0
        if width > self.screen_width:
            scale = self.screen_width / width
        elif height > self.screen_height:
            scale = self.screen_height / height
        return int(width * scale), int(height * scale)

    @staticmethod
    def await_decision(selector, decisions):
        is_selected = Interface.get_keystroke() == selector
        return decisions[is_selected]

    @staticmethod
    def get_keystroke(timeout=WAIT_INFINITELY):
        return cv2.waitKey(timeout)

    @staticmethod
    def clear_screen():
        cv2.destroyAllWindows()


class WelcomingInterface(Interface):
    def __init__(self, resolution_string, welcome_image_path=MATT_PATH):
        super().__init__(resolution_string)
        self.welcome_image_path = welcome_image_path

    def welcome_and_get_decision_key(self):
        print("Press key used for selecting images")
        super().display_picture("Hello there", self.welcome_image_path)
        return super().get_keystroke()
