import cv2

from stsv.decisions import Decision

WAIT_INFINITELY = 0


class Interface:
    @staticmethod
    def display_picture(caption, image):
        cv2.destroyAllWindows()
        cv2.imshow(caption, image)

    @staticmethod
    def get_decision(selector, positive_decision, negative_decision):
        return Decision.SELECT if Interface.get_keystroke(WAIT_INFINITELY) == selector else Decision.DISCARD

    @staticmethod
    def get_keystroke(timeout=WAIT_INFINITELY):
        return cv2.waitKey(timeout)

    @staticmethod
    def clear_screen():
        cv2.destroyAllWindows()
