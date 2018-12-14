import cv2
import os
import pkg_resources

MATT = os.path.join("pics", "matt.png")
MATT_PATH = pkg_resources.resource_filename(__name__, MATT)


class Interface:
    WAIT_INFINITELY = 0

    @staticmethod
    def display_picture(caption, image_path):
        cv2.destroyAllWindows()
        cv2.imshow(caption, cv2.imread(image_path))

    @staticmethod
    def get_decision(selector, decisions):
        is_selected = Interface.get_keystroke() == selector
        return decisions[is_selected]

    @staticmethod
    def get_keystroke(timeout=WAIT_INFINITELY):
        return cv2.waitKey(timeout)

    @staticmethod
    def clear_screen():
        cv2.destroyAllWindows()


class WelcomingInterface(Interface):
    def __init__(self, welcome_image_path=MATT_PATH):
        self.welcome_image_path = welcome_image_path

    def welcome_and_get_decision_key(self):
        print("Press key used for selecting images")
        super().display_picture("Hello there", self.welcome_image_path)
        return super().get_keystroke()

