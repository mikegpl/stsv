import os
import cv2
import numpy as np


def list_pics(pictures_directory_path):
    files = [file for file in os.listdir(pictures_directory_path) if file.endswith(".jpg")]
    return files


def full_path(base, local):
    return "{}/{}".format(base, local)


def create_dir(base, dirname):
    try:
        path = full_path(base, dirname)
        os.makedirs(path)
        return True
    except FileExistsError:
        return False


def move_file_to_dir(base, file, dir_path):
    full_file_path = full_path(base, file)
    full_dir_path = full_path(base, dir_path)
    full_new_path = full_path(full_dir_path, file)
    os.rename(full_file_path, full_new_path)


pics_dir = input("Enter dir where pics are located: ")
print(list_pics(pics_dir))
cv2.imshow("asdf", 200 * np.ones((100, 100)))
print("press key to select")
left = cv2.waitKey(0)
print("press key to discard")
right = cv2.waitKey(0)

selekto_or_diskardo = []
pikczers = list_pics(pics_dir)

create_dir(pics_dir, "select")
create_dir(pics_dir, "discard")

for i in range(len(pikczers)):
    pic = pikczers[i]
    image = cv2.imread(full_path(pics_dir, pic))
    cv2.imshow("", image)
    decyżyn = "S" if cv2.waitKey(0) == left else "D"
    selekto_or_diskardo.append(decyżyn)

print(list(zip(selekto_or_diskardo, pikczers)))
cv2.destroyAllWindows()

for i in range(len(selekto_or_diskardo)):
    target = "select" if selekto_or_diskardo[i] == "S" else "discard"
    move_file_to_dir(pics_dir, pikczers[i], target)
